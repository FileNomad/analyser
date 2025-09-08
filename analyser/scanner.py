from __future__ import annotations
from pathlib import Path
from typing import Iterable
from .metrics import measure_python_source, FileMetrics

def iter_py_files(root: Path, exclude_globs: Iterable[str] = ("*/.venv/*", "*/venv/*", "*/.git/*")):
    for p in root.rglob("*.py"):
        if any(p.match(g) for g in exclude_globs):
            continue
        yield p

def scan(root: str | Path) -> list[FileMetrics]:
    root = Path(root)
    results: list[FileMetrics] = []
    for path in iter_py_files(root):
        try:
            src = path.read_text(encoding="utf-8", errors="ignore")
            results.append(measure_python_source(str(path), src))
        except Exception:
            pass
    return results
