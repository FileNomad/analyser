from __future__ import annotations
import ast
from dataclasses import dataclass

@dataclass
class FileMetrics:
    path: str
    lines: int
    imports: int
    functions: int
    classes: int
    complexity: int

def _node_complexity(node: ast.AST) -> int:
    bumps = (ast.If, ast.For, ast.While, ast.With, ast.ExceptHandler,
             ast.BoolOp, ast.IfExp, ast.Try, ast.Match)
    comp = 1
    for n in ast.walk(node):
        if isinstance(n, bumps):
            comp += 1
    return comp

def measure_python_source(path: str, src: str) -> FileMetrics:
    tree = ast.parse(src, filename=path)
    imports = sum(isinstance(n, (ast.Import, ast.ImportFrom)) for n in ast.walk(tree))
    functions = sum(isinstance(n, ast.FunctionDef) for n in ast.walk(tree))
    classes = sum(isinstance(n, ast.ClassDef) for n in ast.walk(tree))
    complexity = _node_complexity(tree)
    lines = src.count("\n") + (0 if src.endswith("\n") else 1 if src else 0)
    return FileMetrics(path, lines, imports, functions, classes, complexity)