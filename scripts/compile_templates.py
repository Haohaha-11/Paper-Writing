#!/usr/bin/env python3
"""Smoke-compile imported templates from temporary copies."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class CompileTarget:
    name: str
    source_dir: Path
    root_file: str


TARGETS = [
    CompileTarget("iclr-2026", ROOT / "templates/upstream/iclr/2026", "iclr2026_conference.tex"),
    CompileTarget("cvpr-2026", ROOT / "templates/upstream/cvpr/2026", "main.tex"),
    CompileTarget("eccv-2026", ROOT / "templates/upstream/eccv/2026", "main.tex"),
    CompileTarget("neurips-2026", ROOT / "templates/upstream/neurips/2026", "neurips_2026.tex"),
    CompileTarget("icml-2026", ROOT / "templates/upstream/icml/2026", "example_paper.tex"),
    CompileTarget("tmi-ieeetran-minimal", ROOT / "examples/minimal_tmi", "main.tex"),
]


def compile_target(target: CompileTarget, keep_logs: bool) -> tuple[bool, str]:
    if not target.source_dir.exists():
        return False, f"missing source dir: {target.source_dir}"
    with tempfile.TemporaryDirectory(prefix=f"pwh-{target.name}-") as tmp:
        workdir = Path(tmp) / "work"
        shutil.copytree(target.source_dir, workdir)
        cmd = [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            target.root_file,
        ]
        proc = subprocess.run(cmd, cwd=workdir, text=True, capture_output=True, check=False)
        pdf = workdir / Path(target.root_file).with_suffix(".pdf")
        if keep_logs:
            log_dir = ROOT / "templates/compile-logs"
            log_dir.mkdir(exist_ok=True)
            (log_dir / f"{target.name}.stdout.log").write_text(proc.stdout)
            (log_dir / f"{target.name}.stderr.log").write_text(proc.stderr)
        if proc.returncode == 0 and pdf.exists():
            return True, "pass"
        tail = "\n".join((proc.stdout + "\n" + proc.stderr).splitlines()[-20:])
        return False, tail


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Return non-zero if any template fails")
    parser.add_argument("--keep-logs", action="store_true", help="Write logs under templates/compile-logs")
    args = parser.parse_args()

    failures = 0
    for target in TARGETS:
        ok, detail = compile_target(target, args.keep_logs)
        status = "PASS" if ok else "FAIL"
        print(f"{status} {target.name}: {detail}")
        failures += 0 if ok else 1

    if args.check and failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
