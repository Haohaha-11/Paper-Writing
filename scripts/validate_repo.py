#!/usr/bin/env python3
"""Lightweight repository validation for the document-first project."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(path: str) -> None:
    if not (ROOT / path).exists():
        fail(f"missing required path: {path}")


def validate_required_paths() -> None:
    for path in [
        "README.md",
        "QUICKSTART.md",
        "AGENTS.md",
        "CONTRIBUTING.md",
        "CITATION.cff",
        "THIRD_PARTY.md",
        "IMPLEMENTATION_STATUS.md",
        "skills/README.md",
        "venues/README.md",
        "workflows/README.md",
        "templates/README.md",
        "templates/import-manifest.json",
        "templates/checksums.sha256",
        "templates/compile-validation.md",
    ]:
        require(path)


def validate_import_manifest() -> None:
    manifest = ROOT / "templates/import-manifest.json"
    data = json.loads(manifest.read_text())
    if not isinstance(data, list) or not data:
        fail("templates/import-manifest.json must contain a non-empty list")
    for item in data:
        for key in ["name", "type", "dest", "files"]:
            if key not in item:
                fail(f"manifest item missing {key}: {item}")
        if not (ROOT / item["dest"]).exists():
            fail(f"manifest destination does not exist: {item['dest']}")


def validate_skill_shape() -> None:
    required_sections = [
        "## Purpose",
        "## When To Use",
        "## Inputs",
        "## Output Contract",
        "## Sources Reviewed",
    ]
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_files:
        fail("no skill files found")
    for path in skill_files:
        text = path.read_text()
        for section in required_sections:
            if section not in text:
                fail(f"{path.relative_to(ROOT)} missing section {section}")


def validate_internal_markdown_links() -> None:
    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(errors="replace")
        for _, target in pattern.findall(text):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            if clean.startswith("/"):
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if not resolved.exists():
                fail(f"broken markdown link in {path.relative_to(ROOT)} -> {target}")


def main() -> None:
    validate_required_paths()
    validate_import_manifest()
    validate_skill_shape()
    validate_internal_markdown_links()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
