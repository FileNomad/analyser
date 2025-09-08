from __future__ import annotations
from rich.table import Table
from .metrics import FileMetrics
import json

def to_table(rows: list[FileMetrics]) -> Table:
    t = Table(title="Analyser — File Metrics")
    t.add_column("File", overflow="fold")
    t.add_column("Lines", justify="right")
    t.add_column("Imports", justify="right")
    t.add_column("Funcs", justify="right")
    t.add_column("Classes", justify="right")
    t.add_column("Complexity", justify="right")
    for m in rows:
        t.add_row(m.path, str(m.lines), str(m.imports), str(m.functions), str(m.classes), str(m.complexity))
    return t

def to_json(rows: list[FileMetrics]) -> str:
    return json.dumps([m.__dict__ for m in rows], indent=2)
