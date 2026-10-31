"""Python AST-based symbol extractor.

Purpose: Extracts an outline of function and class names, argument signatures, and line spans from Python files.
Phase: Phase 0 (Foundation stub), implemented in Phase 2.
Serves: Code Locator agent via repo MCP server.
"""

from pathlib import Path

from clarify_or_code.agents.schemas import SymbolInfo


def extract_symbols(file_path: Path) -> list[SymbolInfo]:
    """Parse a Python source file using standard ast and return function and class outlines.

    Args:
        file_path: Absolute or relative path to the Python source file.

    Returns:
        List of SymbolInfo models detailing symbol name, kind, line range, and signature.
    """
    raise NotImplementedError("AST symbol outline extraction stub. Implemented in Phase 2.")
