"""
server.py — Remote UX Pattern Oracle via FastMCP.

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
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WIKI_DIR   = Path("wiki")
GRAPH_FILE = Path("graphify-out") / "graph.json"

# ---------------------------------------------------------------------------
# Startup: compile brain if needed
# ---------------------------------------------------------------------------

def _wiki_has_content() -> bool:
    return WIKI_DIR.exists() and any(WIKI_DIR.glob("*.md"))


def _compile_graph() -> None:
    """Run graphify against ./wiki and write graphify-out/graph.json."""
    print("[oracle] graphify-out/graph.json not found — compiling knowledge graph …", flush=True)
    GRAPH_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Try Ollama backend first (no API key needed), then fall back to default
    backend_args = ["--backend", "ollama"] if os.getenv("OLLAMA_HOST") or _ollama_available() else []
    cmd = ["graphify", str(WIKI_DIR), "--no-viz"] + backend_args

    print(f"[oracle] Running: {' '.join(cmd)}", flush=True)
    result = subprocess.run(
        cmd,
        capture_output=False,   # stream stdout/stderr directly to cloud logs
        text=True,
    )

    if result.returncode != 0:
        # If Ollama failed and we tried it, retry without backend flag
        if backend_args:
            print("[oracle] Ollama backend failed, retrying with default backend...", flush=True)
            cmd = ["graphify", str(WIKI_DIR), "--no-viz"]
            result = subprocess.run(
                cmd,
                capture_output=False,
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
            "source_file": str(md_file)
        })
    
    # Create basic links between adjacent files
    for i in range(len(nodes) - 1):
        links.append({
            "source": nodes[i]["id"],
            "target": nodes[i+1]["id"],
            "relation": "adjacency"
        })
    
    graph = {"nodes": nodes, "links": links}
    GRAPH_FILE.write_text(json.dumps(graph, indent=2), encoding="utf-8")
    print(f"[oracle] Basic graph generated with {len(nodes)} nodes and {len(links)} links.", flush=True)


def _ollama_available() -> bool:
    """Check if Ollama is available locally."""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            timeout=2,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _startup_check() -> None:
    if not _wiki_has_content():
        print("[oracle] WARN: ./wiki is empty or missing. Run ingest.py first.", flush=True)
        return  # server still starts — tools will return helpful messages

    if not GRAPH_FILE.exists():
        _compile_graph()
    else:
        print(f"[oracle] graph.json found at {GRAPH_FILE} — skipping compilation.", flush=True)


# ---------------------------------------------------------------------------
# Graph helpers
# ---------------------------------------------------------------------------

def _load_graph() -> dict[str, Any]:
    if not GRAPH_FILE.exists():
        return {}
    return json.loads(GRAPH_FILE.read_text(encoding="utf-8"))


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
    return (
        f"**{node.get('label', node['id'])}**  "
        f"(type: {node.get('file_type', '?')}, "
        f"source: {node.get('source_file', '?')})"
    )


# ---------------------------------------------------------------------------
# MCP server + tools
# ---------------------------------------------------------------------------

mcp = FastMCP("UX_Pattern_Oracle")


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> JSONResponse:
    graph_ready = GRAPH_FILE.exists()
    return JSONResponse({
        "status": "ok",
        "graph": "ready" if graph_ready else "not_compiled",
    })


@mcp.tool()
def ask_ux_oracle(query: str) -> str:
    """
    Search the UX pattern knowledge graph for concepts matching the query.
    Returns the most relevant patterns with their graph relationships.
    """
    graph = _load_graph()
    if not graph:
        return "Knowledge graph not available. Ensure wiki/ contains .md files and restart the server."

    matches = _find_nodes(graph, query, top_k=5)
    if not matches:
        return f"No patterns found matching '{query}'. Try broader terms."

    lines = [f"## Oracle results for: '{query}'\n"]
    for node in matches:
        lines.append(_node_summary(node))
        neighbours = _neighbours(graph, node["id"])
        if neighbours:
            related = ", ".join(n.get("label", n["id"]) for n in neighbours[:6])
            lines.append(f"  → Connected to: {related}")
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def get_pattern_psychology(pattern_name: str) -> str:
    """
    Retrieve the cognitive and psychological underpinnings of a UX pattern.
    Returns the pattern node, its wiki content, and psychologically-related neighbours.
    """
    graph = _load_graph()
    if not graph:
        return "Knowledge graph not available."

    matches = _find_nodes(graph, pattern_name, top_k=1)
    if not matches:
        return f"Pattern '{pattern_name}' not found in the knowledge graph."

    node       = matches[0]
    neighbours = _neighbours(graph, node["id"])

    # Try to pull wiki content
    src = node.get("source_file", "")
    wiki_path = Path(src) if src.startswith("wiki/") else WIKI_DIR / f"{node.get('norm_label', '').replace(' ', '-')}.md"
    wiki_content = ""
    if wiki_path.exists():
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
    return "\n".join(lines)


@mcp.tool()
def generate_design_spec(pattern_name: str, target_platform: str) -> str:
    """
    Generate a platform-specific design specification for a UX pattern.
    target_platform examples: 'iOS', 'Android', 'web', 'desktop', 'voice'.
    """
    graph = _load_graph()
    if not graph:
        return "Knowledge graph not available."

    matches = _find_nodes(graph, pattern_name, top_k=1)
    if not matches:
        return f"Pattern '{pattern_name}' not found."

    node          = matches[0]
    neighbours    = _neighbours(graph, node["id"])
    label         = node.get("label", pattern_name)
    platform      = target_platform.strip()
    related_labels = [n.get("label", n["id"]) for n in neighbours[:8]]
    related_str   = "\n".join(f"  - {l}" for l in related_labels) if related_labels else "  (none found)"

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
def predict_component_states(component_name: str) -> str:
    """
    Predict all possible UI states for a component by traversing the knowledge graph.
    Returns: default, hover, focus, active, disabled, error, loading, empty — where evidenced.
    """
    graph = _load_graph()
    if not graph:
        return "Knowledge graph not available."

    matches = _find_nodes(graph, component_name, top_k=1)
    if not matches:
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
