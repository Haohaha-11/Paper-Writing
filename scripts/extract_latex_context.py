#!/usr/bin/env python3
"""Extract lightweight structure from a LaTeX paper tree.

This script is intentionally conservative. It does not try to fully parse TeX;
it finds common project context that writing/review agents need before editing.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


COMMAND_PATTERNS = {
    "inputs": re.compile(r"\\(?:input|include)\{([^}]+)\}"),
    "bibliographies": re.compile(r"\\(?:bibliography|addbibresource)\{([^}]+)\}"),
    "figures": re.compile(r"\\(?:includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}"),
    "styles": re.compile(r"\\(?:usepackage|documentclass)(?:\[[^\]]*\])?\{([^}]+)\}"),
}


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        escaped = False
        kept = []
        for char in line:
            if char == "%" and not escaped:
                break
            kept.append(char)
            escaped = char == "\\" and not escaped
        lines.append("".join(kept))
    return "\n".join(lines)


def split_brace_list(value: str) -> list[str]:
    return [part.strip() for part in value.split(",") if part.strip()]


def with_tex_suffix(path: Path) -> Path:
    if path.suffix:
        return path
    return path.with_suffix(".tex")


def find_roots(root_dir: Path) -> list[Path]:
    roots = []
    for path in sorted(root_dir.rglob("*.tex")):
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        if "\\documentclass" in text and "\\begin{document}" in text:
            roots.append(path)
    return roots


def resolve_existing(base: Path, value: str, suffixes: Iterable[str]) -> str:
    raw = Path(value)
    candidates = [base / raw]
    if not raw.suffix:
        candidates.extend((base / raw).with_suffix(suffix) for suffix in suffixes)
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return str(base / raw)


def scan_file(path: Path, seen: set[Path], result: dict[str, object]) -> None:
    resolved = path.resolve()
    if resolved in seen or not path.exists():
        return
    seen.add(resolved)

    text = strip_comments(path.read_text(errors="replace"))
    rel = str(path)
    result["scanned_files"].append(rel)

    if "\\appendix" in text or "\\begin{appendices}" in text:
        result["appendix_markers"].append(rel)

    base = path.parent
    for key, pattern in COMMAND_PATTERNS.items():
        for match in pattern.findall(text):
            for value in split_brace_list(match):
                if key == "inputs":
                    target = with_tex_suffix(base / value)
                    result[key].append(str(target))
                    scan_file(target, seen, result)
                elif key == "bibliographies":
                    result[key].append(resolve_existing(base, value, [".bib"]))
                elif key == "figures":
                    result[key].append(resolve_existing(base, value, [".pdf", ".png", ".jpg", ".jpeg", ".eps"]))
                else:
                    result[key].append(value)


def dedupe(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="LaTeX root file or project directory")
    parser.add_argument("--root", help="Explicit root .tex file")
    args = parser.parse_args()

    base = Path(args.path).resolve()
    if args.root:
        roots = [Path(args.root).resolve()]
    elif base.is_file():
        roots = [base]
        base = base.parent
    else:
        roots = find_roots(base)

    result: dict[str, object] = {
        "project": str(base),
        "roots": [str(path) for path in roots],
        "scanned_files": [],
        "inputs": [],
        "bibliographies": [],
        "figures": [],
        "styles": [],
        "appendix_markers": [],
    }

    seen: set[Path] = set()
    for root in roots:
        scan_file(root, seen, result)

    for key in ["scanned_files", "inputs", "bibliographies", "figures", "styles", "appendix_markers"]:
        result[key] = dedupe(result[key])

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
