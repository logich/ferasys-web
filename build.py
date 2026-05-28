#!/usr/bin/env python3
"""Static site assembler for ferasys.com.

Reads:
  - partials/header.html  — DOCTYPE through end of <header> (nav). Contains
    {{placeholder}} substitutions filled from per-page front-matter.
  - partials/footer.html  — <footer> through closing </html>. Shared across
    every page. Carries the global JSON-LD graph and scripts.
  - pages/*.html          — one file per page. First lines are key: value
    front-matter, terminated by a line containing only "---". Body follows.

Writes:
  - _site/<page>.html     — assembled HTML for each input page.

This is a deliberately small script. No template engine, no dependencies
beyond the Python stdlib. Substitution is a single regex pass; front-matter
parsing is split-on-first "---".

Usage:
    python3 build.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
PARTIALS = ROOT / "partials"
PAGES = ROOT / "pages"
OUT = ROOT / "_site"

PLACEHOLDER_RE = re.compile(r"\{\{\s*(\w+)\s*\}\}")
FRONTMATTER_RE = re.compile(r"\A(.*?)\n---\s*\n(.*)", re.DOTALL)


def parse_page(path: Path) -> tuple[dict[str, str], str]:
    """Split front-matter from body. Returns (meta, body)."""
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    header, body = match.groups()
    meta: dict[str, str] = {}
    for line in header.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta, body


def substitute(template: str, vars: dict[str, str], context: str) -> str:
    """Replace {{key}} placeholders. Warns if a key is unresolved."""
    missing: list[str] = []

    def repl(m: re.Match[str]) -> str:
        key = m.group(1)
        if key in vars:
            return vars[key]
        missing.append(key)
        return m.group(0)

    out = PLACEHOLDER_RE.sub(repl, template)
    if missing:
        print(
            f"  warning: unresolved placeholders in {context}: {sorted(set(missing))}",
            file=sys.stderr,
        )
    return out


def build() -> int:
    if not PARTIALS.exists() or not PAGES.exists():
        print(f"missing partials/ or pages/ at {ROOT}", file=sys.stderr)
        return 1

    header_tpl = (PARTIALS / "header.html").read_text(encoding="utf-8")
    footer_tpl = (PARTIALS / "footer.html").read_text(encoding="utf-8")

    OUT.mkdir(exist_ok=True)
    page_files = sorted(PAGES.glob("*.html"))
    if not page_files:
        print(f"no pages found in {PAGES}", file=sys.stderr)
        return 1

    for src in page_files:
        meta, body = parse_page(src)
        header = substitute(header_tpl, meta, f"{src.name} (header)")
        footer = substitute(footer_tpl, meta, f"{src.name} (footer)")
        rendered = header + body + footer
        dst = OUT / src.name
        dst.write_text(rendered, encoding="utf-8")
        print(f"  built {src.name} -> _site/{src.name}")

    return 0


if __name__ == "__main__":
    sys.exit(build())
