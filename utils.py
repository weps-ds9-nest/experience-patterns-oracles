"""
utils.py — Shared utility functions for the Experience Patterns Oracle scripts.
"""

import ipaddress
import re
from pathlib import Path
from urllib.parse import urlparse

BLOCKED_NETWORKS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),   # link-local / cloud metadata
    ipaddress.ip_network("127.0.0.0/8"),       # loopback
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
]


def validate_url(url: str) -> None:
    """Raise ValueError if the URL is not a safe external HTTP/HTTPS URL."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Blocked non-HTTP scheme: {parsed.scheme!r}")
    hostname = parsed.hostname or ""
    try:
        addr = ipaddress.ip_address(hostname)
        for net in BLOCKED_NETWORKS:
            if addr in net:
                raise ValueError(f"Blocked private/link-local IP: {addr}")
    except ValueError as e:
        if "Blocked" in str(e):
            raise
        # Hostname is a domain name, proceed


def safe_output_path(directory: Path, slug: str, resolved_base: Path) -> Path:
    """Return resolved path to output file if it stays inside the base directory, otherwise raise ValueError."""
    candidate = (directory / f"{slug}.md").resolve()
    if not candidate.is_relative_to(resolved_base):
        raise ValueError(f"Slug '{slug}' escapes output directory")
    return candidate


def slugify(text: str) -> str:
    """Convert a title or URL into a clean, safe filename slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text).strip("-")
