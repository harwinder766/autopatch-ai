"""Ripgrep wrapper for agentic code search.

Purpose: Performs fast keyword and regex code searching with line numbers and bounds.
Phase: Phase 0 (Foundation stub), implemented in Phase 2.
Serves: Code Locator agent via repo MCP server.
"""

from pathlib import Path
from typing import Any


class CodeSearcher:
    """Agentic search engine wrapping ripgrep and file reading."""

    def __init__(self, workspace_path: Path) -> None:
        self.workspace_path = workspace_path

    def search_pattern(
        self,
        query: str,
        path_pattern: str | None = None,
        max_matches: int = 50,
    ) -> list[dict[str, Any]]:
        """Execute ripgrep search with line numbers across non-ignored files."""
        raise NotImplementedError("Ripgrep search stub. Implemented in Phase 2.")

    def read_file_slice(
        self,
        relative_path: str,
        start_line: int | None = None,
        end_line: int | None = None,
    ) -> str:
        """Read specific line range of a file in the workspace."""
        raise NotImplementedError("Bounded file reading stub. Implemented in Phase 2.")
