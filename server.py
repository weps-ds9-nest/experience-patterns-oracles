"""
server.py — Public UX Pattern Oracle via FastMCP.

This is a publicly accessible MCP server for consulting UX and Behavioural
Design Patterns. No authentication required — rate-limited to prevent abuse.

Startup sequence
----------------
1. Ensure ./wiki contains at least one .md file.
2. If graphify-out/graph.json is missing, run `graphify ./wiki --no-viz`
   so the container compiles its own knowledge graph before serving.
3. Start FastMCP over HTTP on $PORT (default 8000).

Tools
-----
- ask_ux_oracle(query)
- get_pattern_psychology(pattern_name)
- generate_design_spec(pattern_name, target_platform)
- predict_component_states(component_name)
"""

import json
import logging
import os
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

from fastmcp import FastMCP, Context
from starlette.requests import Request
from starlette.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# API key for authentication (optional but recommended)
API_KEY = os.getenv("MCP_API_KEY")

# Module-level graph cache
_graph_cache: dict[str, Any] | None = None
_graph_mtime: float = 0.0

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WIKI_DIR   = Path("wiki")
GRAPH_FILE = Path("graphify-out") / "graph.json"

_WIKI_DIR_RESOLVED = WIKI_DIR.resolve()


def _safe_wiki_path(norm_label: str) -> Path | None:
    """Return a resolved wiki path only if it stays inside WIKI_DIR."""
    if not norm_label:
        return None
    candidate = (WIKI_DIR / f"{norm_label.replace(' ', '-')}.md").resolve()
    if candidate.is_relative_to(_WIKI_DIR_RESOLVED):
        return candidate
    return None


# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------
def _check_auth(request: Request) -> bool:
    """Check if request has valid API key if one is configured."""
    if not API_KEY:
        # No API key configured - allow all requests
        return True
    provided_key = request.headers.get("X-API-Key")
    return provided_key == API_KEY


# ---------------------------------------------------------------------------
# Rate limiting (in-memory, simple to prevent abuse)
# ---------------------------------------------------------------------------
# Rate limit: 60 requests per minute per IP
RATE_LIMIT_REQUESTS = 60
RATE_LIMIT_WINDOW = 60  # seconds

_request_counts: dict[str, list[float]] = defaultdict(list)


def _check_rate_limit(client_ip: str) -> bool:
    """Check if client IP is within rate limits. Returns True if allowed."""
    # TODO: If scaling to multiple processes/workers, back this rate limiter with a shared store (e.g. Redis).
    now = time.time()
    
    # Prune inactive IPs to prevent memory leaks
    for ip in list(_request_counts.keys()):
        active_ts = [t for t in _request_counts[ip] if now - t < RATE_LIMIT_WINDOW]
        if not active_ts:
            del _request_counts[ip]
        else:
            _request_counts[ip] = active_ts
    
    # Check if under limit
    if len(_request_counts[client_ip]) < RATE_LIMIT_REQUESTS:
        _request_counts[client_ip].append(now)
        return True
    
    return False

# ---------------------------------------------------------------------------
# Startup: compile brain if needed
# ---------------------------------------------------------------------------

def _wiki_has_content() -> bool:
    return WIKI_DIR.exists() and any(WIKI_DIR.glob("*.md"))


def _compile_graph() -> None:
    """Run graphify against ./wiki and write graphify-out/graph.json."""
    print("[oracle] graphify-out/graph.json not found — compiling knowledge graph …", flush=True)
    GRAPH_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Only use LLM backend if explicitly enabled via GRAPHIFY_USE_LLM
    use_llm = os.getenv("GRAPHIFY_USE_LLM", "").lower() in ("true", "1", "yes")
    
    if use_llm:
        # User explicitly requested LLM backend
        backend = os.getenv("GRAPHIFY_BACKEND", "ollama")
        model = os.getenv("GRAPHIFY_MODEL", "")
        backend_args = ["--backend", backend]
        model_args = ["--model", model] if model else []
        cmd = ["graphify", str(WIKI_DIR), "--no-viz"] + backend_args + model_args
    else:
        # Default: use basic graph generation (no LLM required)
        cmd = ["graphify", str(WIKI_DIR), "--no-viz"]

    print(f"[oracle] Running: {' '.join(cmd)}", flush=True)
    result = subprocess.run(
        cmd,
        capture_output=False,   # stream stdout/stderr directly to cloud logs
        text=True,
    )

    if result.returncode != 0:
        print("[oracle] Graphify failed, falling back to basic graph generator...", flush=True)
        _compile_basic_graph()
        return

    if not GRAPH_FILE.exists():
        print("[oracle] ERROR: graph.json was not produced — check graphify output above.", file=sys.stderr, flush=True)
        sys.exit(1)

    print("[oracle] Knowledge graph compiled successfully.", flush=True)


def _compile_basic_graph() -> None:
    """Generate a basic graph from wiki files without LLM."""
    print("[oracle] Generating basic graph from wiki files...", flush=True)
    
    nodes = []
    links = []
    
    for i, md_file in enumerate(sorted(WIKI_DIR.glob("*.md"))):
        if md_file.name == ".gitkeep":
            continue
            
        content = md_file.read_text(encoding="utf-8")
        # Extract title from first heading or filename
        first_line = content.split("\n")[0].strip()
        if first_line.startswith("#"):
            title = first_line.lstrip("#").strip()
        else:
            title = md_file.stem.replace("-", " ").title()
        
        nodes.append({
            "id": i,
            "label": title,
            "norm_label": md_file.stem,
            "file_type": "markdown",
            "source_file": str(md_file.resolve().relative_to(_WIKI_DIR_RESOLVED))
        })
    
    # Create basic links between adjacent files
    for i in range(len(nodes) - 1):
        links.append({
            "source": nodes[i]["id"],
            "target": nodes[i+1]["id"],
            "relation": "adjacency"
        })
    
    graph = {
        "graph_type": "basic-adjacency",
        "nodes": nodes,
        "links": links
    }
    GRAPH_FILE.write_text(json.dumps(graph, indent=2), encoding="utf-8")
    print(f"[oracle] Basic graph generated with {len(nodes)} nodes and {len(links)} links.", flush=True)


def _startup_check() -> None:
    if not _wiki_has_content():
        print("[oracle] WARN: ./wiki is empty or missing. Run ingest.py first.", flush=True)
        return  # server still starts — tools will return helpful messages

    if not GRAPH_FILE.exists():
        _compile_graph()
    else:
        print(f"[oracle] graph.json found at {GRAPH_FILE} — skipping compilation.", flush=True)

    # Check graph quality
    try:
        graph = _load_graph()
        if graph.get("graph_type") == "basic-adjacency":
            print("[oracle] WARN: Graph uses basic adjacency links only. Run graphify with an LLM backend for semantic relationships.", flush=True)
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Graph helpers
# ---------------------------------------------------------------------------

def _nodes(graph: dict) -> list[dict]:
    return graph.get("nodes", [])


def _links(graph: dict) -> list[dict]:
    # NetworkX node-link format uses "links" not "edges"
    return graph.get("links", graph.get("edges", []))


def _normalize(text: str) -> str:
    return text.lower().replace("-", " ").replace("_", " ")


def _find_nodes(graph: dict, query: str, top_k: int = 5) -> list[dict]:
    """Return up to top_k nodes whose label or norm_label contains the query."""
    q = _normalize(query)
    scored: list[tuple[int, dict]] = []

    for node in _nodes(graph):
        label      = _normalize(node.get("label", ""))
        norm_label = _normalize(node.get("norm_label", ""))
        score = 0
        if q in label:
            score += 2
        if q in norm_label:
            score += 1
        for word in q.split():
            if word in label or word in norm_label:
                score += 1
        if score:
            scored.append((score, node))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [n for _, n in scored[:top_k]]


def _neighbours(graph: dict, node_id: str) -> list[dict]:
    """Return all nodes directly connected to node_id."""
    ids: set[str] = set()
    for link in _links(graph):
        if link.get("source") == node_id:
            ids.add(str(link["target"]))
        elif link.get("target") == node_id:
            ids.add(str(link["source"]))

    id_map = {str(n["id"]): n for n in _nodes(graph)}
    return [id_map[i] for i in ids if i in id_map]


def _node_summary(node: dict) -> str:
    return f"**{node.get('label', node['id'])}** (type: {node.get('file_type', '?')})"


def _validate_graph(graph: dict) -> dict:
    """Validate all source_file attributes in graph nodes stay inside WIKI_DIR."""
    safe_nodes = []
    for node in _nodes(graph):
        src = node.get("source_file", "")
        if src:
            try:
                p = Path(src).resolve()
                if not p.is_relative_to(_WIKI_DIR_RESOLVED):
                    p = (WIKI_DIR / src).resolve()
                if not p.is_relative_to(_WIKI_DIR_RESOLVED):
                    print(f"[oracle] WARN: blocked unsafe source_file in graph: {src}", flush=True)
                    node = {**node, "source_file": ""}
            except Exception:
                node = {**node, "source_file": ""}
        safe_nodes.append(node)
    graph["nodes"] = safe_nodes
    return graph


def _load_graph() -> dict[str, Any]:
    global _graph_cache, _graph_mtime
    if not GRAPH_FILE.exists():
        return {}
    try:
        mtime = GRAPH_FILE.stat().st_mtime
        if _graph_cache is not None and mtime == _graph_mtime:
            return _graph_cache
        graph = json.loads(GRAPH_FILE.read_text(encoding="utf-8"))
        _graph_cache = _validate_graph(graph)
        _graph_mtime = mtime
        return _graph_cache
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# MCP server + tools
# ---------------------------------------------------------------------------

mcp = FastMCP("UX_Pattern_Oracle")


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> JSONResponse:
    if not _check_auth(request):
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    logger.info("Health check requested")
    return JSONResponse({"status": "ok"})


@mcp.tool()
def ask_ux_oracle(query: str, ctx: Context = None) -> str:
    """
    Search the UX pattern knowledge graph for concepts matching the query.
    Returns the most relevant patterns with their graph relationships.
    """
    # Input validation
    if len(query) > 1000:
        return "Query too long. Maximum 1000 characters."

    client_id = ctx.client_id if (ctx and ctx.client_id) else "tool_global"
    logger.info(f"ask_ux_oracle request from {client_id}: query='{query[:50]}...'")

    if not _check_rate_limit(client_id):
        logger.warning(f"Rate limit exceeded for {client_id}")
        return "Rate limit exceeded. Please wait a moment before making more requests."

    graph = _load_graph()
    if not graph:
        logger.warning("Knowledge graph not available")
        return "Knowledge graph not available. Ensure wiki/ contains .md files and restart the server."

    matches = _find_nodes(graph, query, top_k=5)
    if not matches:
        logger.info(f"No patterns found matching '{query}'")
        return f"No patterns found matching '{query}'. Try broader terms."

    lines = [f"## Oracle results for: '{query}'\n"]
    for node in matches:
        lines.append(_node_summary(node))
        neighbours = _neighbours(graph, node["id"])
        if neighbours:
            related = ", ".join(n.get("label", n["id"]) for n in neighbours[:6])
            lines.append(f"  → Connected to: {related}")
        lines.append("")

    logger.info(f"ask_ux_oracle completed successfully for {client_id}")
    return "\n".join(lines)


@mcp.tool()
def get_pattern_psychology(pattern_name: str, ctx: Context = None) -> str:
    """
    Retrieve the cognitive and psychological underpinnings of a UX pattern.
    Returns the pattern node, its wiki content, and psychologically-related neighbours.
    """
    # Input validation
    if len(pattern_name) > 500:
        return "Pattern name too long. Maximum 500 characters."

    client_id = ctx.client_id if (ctx and ctx.client_id) else "tool_global"
    logger.info(f"get_pattern_psychology request from {client_id}: pattern='{pattern_name}'")

    if not _check_rate_limit(client_id):
        logger.warning(f"Rate limit exceeded for {client_id}")
        return "Rate limit exceeded. Please wait a moment before making more requests."

    graph = _load_graph()
    if not graph:
        logger.warning("Knowledge graph not available")
        return "Knowledge graph not available."

    matches = _find_nodes(graph, pattern_name, top_k=1)
    if not matches:
        logger.info(f"Pattern '{pattern_name}' not found")
        return f"Pattern '{pattern_name}' not found in the knowledge graph."

    node       = matches[0]
    neighbours = _neighbours(graph, node["id"])

    # Safely pull wiki content
    norm_label = node.get('norm_label', '')
    wiki_path = _safe_wiki_path(norm_label)
    wiki_content = ""
    if wiki_path and wiki_path.exists():
        # Check size before reading
        if wiki_path.stat().st_size <= 1_000_000:
            wiki_content = f"\n\n### Wiki entry\n{wiki_path.read_text(encoding='utf-8')[:1500]}"

    psych_keywords = {"cognitive", "mental", "bias", "heuristic", "load", "attention",
                      "memory", "perception", "gestalt", "feedback", "affordance", "principle"}
    psych_neighbours = [
        n for n in neighbours
        if any(kw in _normalize(n.get("label", "")) for kw in psych_keywords)
    ]

    lines = [f"## Psychology of: {node.get('label', pattern_name)}\n", _node_summary(node)]
    if psych_neighbours:
        lines.append("\n### Psychologically linked concepts")
        for n in psych_neighbours:
            lines.append(f"- {_node_summary(n)}")
    elif neighbours:
        lines.append("\n### Related concepts")
        for n in neighbours[:6]:
            lines.append(f"- {_node_summary(n)}")

    lines.append(wiki_content)
    logger.info(f"get_pattern_psychology completed successfully for {client_id}")
    return "\n".join(lines)


@mcp.tool()
def generate_design_spec(pattern_name: str, target_platform: str, ctx: Context = None) -> str:
    """
    Generate a platform-specific design specification for a UX pattern.
    target_platform examples: 'iOS', 'Android', 'web', 'desktop', 'voice'.
    """
    # Input validation
    if len(pattern_name) > 500:
        return "Pattern name too long. Maximum 500 characters."
    if len(target_platform) > 100:
        return "Platform name too long. Maximum 100 characters."

    client_id = ctx.client_id if (ctx and ctx.client_id) else "tool_global"
    logger.info(f"generate_design_spec request from {client_id}: pattern='{pattern_name}', platform='{target_platform}'")

    if not _check_rate_limit(client_id):
        logger.warning(f"Rate limit exceeded for {client_id}")
        return "Rate limit exceeded. Please wait a moment before making more requests."

    graph = _load_graph()
    if not graph:
        logger.warning("Knowledge graph not available")
        return "Knowledge graph not available."

    matches = _find_nodes(graph, pattern_name, top_k=1)
    if not matches:
        logger.info(f"Pattern '{pattern_name}' not found")
        return f"Pattern '{pattern_name}' not found."

    node          = matches[0]
    neighbours    = _neighbours(graph, node["id"])
    label         = node.get("label", pattern_name)
    platform      = target_platform.strip()
    related_labels = [n.get("label", n["id"]) for n in neighbours[:8]]
    related_str   = "\n".join(f"  - {l}" for l in related_labels) if related_labels else "  (none found)"

    logger.info(f"generate_design_spec completed successfully for {client_id}")
    return f"""## Design Specification — {label} on {platform}

### Pattern
{label}

### Target Platform
{platform}

### Graph-derived Context
The following concepts are directly connected to this pattern in the knowledge graph:
{related_str}

### Specification Outline
1. **Intent** — Describe the core user problem this pattern solves on {platform}.
2. **Trigger** — Define the condition or user action that activates this pattern.
3. **Behaviour** — Step-by-step interaction flow adhering to {platform} conventions.
4. **Visual Design** — Layout, spacing, and component tokens per {platform} guidelines.
5. **Accessibility** — {platform}-specific a11y requirements (WCAG 2.2 AA minimum).
6. **Edge Cases** — Error states, empty states, loading states.
7. **Related Patterns** — {', '.join(related_labels[:4]) if related_labels else 'N/A'}

> Populate each section using the wiki entry and graph neighbours above.
"""


@mcp.tool()
def predict_component_states(component_name: str, ctx: Context = None) -> str:
    """
    Predict all possible UI states for a component by traversing the knowledge graph.
    Returns: default, hover, focus, active, disabled, error, loading, empty — where evidenced.
    """
    # Input validation
    if len(component_name) > 500:
        return "Component name too long. Maximum 500 characters."

    client_id = ctx.client_id if (ctx and ctx.client_id) else "tool_global"
    logger.info(f"predict_component_states request from {client_id}: component='{component_name}'")

    if not _check_rate_limit(client_id):
        logger.warning(f"Rate limit exceeded for {client_id}")
        return "Rate limit exceeded. Please wait a moment before making more requests."

    graph = _load_graph()
    if not graph:
        logger.warning("Knowledge graph not available")
        return "Knowledge graph not available."

    matches = _find_nodes(graph, component_name, top_k=1)
    if not matches:
        logger.info(f"Component '{component_name}' not found")
        return f"Component '{component_name}' not found in the knowledge graph."

    node       = matches[0]
    neighbours = _neighbours(graph, node["id"])
    label      = node.get("label", component_name)

    state_keywords: dict[str, list[str]] = {
        "default":  ["default", "rest", "idle", "normal"],
        "hover":    ["hover", "mouseover", "pointer"],
        "focus":    ["focus", "keyboard", "tab", "accessible"],
        "active":   ["active", "pressed", "click", "tap", "selected"],
        "disabled": ["disabled", "inactive", "unavailable", "readonly"],
        "error":    ["error", "invalid", "validation", "fail", "warning"],
        "loading":  ["loading", "skeleton", "spinner", "pending", "fetching"],
        "empty":    ["empty", "zero", "blank", "no data", "placeholder"],
    }

    detected: dict[str, list[str]] = {}
    for state, keywords in state_keywords.items():
        evidence = [
            n.get("label", n["id"])
            for n in ([node] + neighbours)
            if any(kw in _normalize(n.get("label", "")) for kw in keywords)
        ]
        if evidence:
            detected[state] = evidence

    lines = [f"## Predicted States — {label}\n"]
    if detected:
        for state, evidence in detected.items():
            lines.append(f"- **{state.capitalize()}** — evidenced by: {', '.join(evidence)}")
    else:
        lines.append("No state-specific nodes found. Consider adding state documentation to the wiki.")

    lines.append(f"\n### All connected concepts ({len(neighbours)} total)")
    for n in neighbours[:10]:
        lines.append(f"  - {n.get('label', n['id'])}")

    logger.info(f"predict_component_states completed successfully for {client_id}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    _startup_check()
    port = int(os.getenv("PORT", "8000"))
    print(f"[oracle] Starting UX Pattern Oracle on http://0.0.0.0:{port}", flush=True)
    mcp.run(transport="http", host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
