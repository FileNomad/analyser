from __future__ import annotations
import typer
from rich.console import Console
from pathlib import Path
from .scanner import scan
from .report import to_table, to_json

app = typer.Typer(help="Static-ish, fast Python project analyser.")

@app.command()
def run(
    path: str = typer.Argument(".", help="Path to project root"),
    json_out: str | None = typer.Option(None, help="Write JSON report to this file"),
):
    results = scan(Path(path))
    console = Console()
    if not results:
        console.print("[yellow]No Python files found.[/yellow]")
        return
    console.print(to_table(results))
    if json_out:
        Path(json_out).write_text(to_json(results), encoding="utf-8")
        console.print(f"\n[bold]JSON written:[/bold] {json_out}")

if __name__ == "__main__":
    app()
