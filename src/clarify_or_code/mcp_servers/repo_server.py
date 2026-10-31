"""FastMCP repository tools server.

Purpose: Exposes repository search, AST symbol outlines, file reads, and patch operations on local git worktrees.
Phase: Phase 0 (Foundation stub), implemented in Phases 2 and 3.
Serves: Code Locator, Fixer, and Reviewer agents.
"""

from typing import Any


def create_repo_mcp_server(workspace_root: str) -> Any:
    """Create and configure the FastMCP repo server instance.

    Tools exposed:
    - search_code(query: str, path_pattern: str | None)
    - read_file(path: str, start_line: int | None, end_line: int | None)
    - list_symbols(path: str)
    - apply_patch(patch: str)
    - git_diff()
    """
    raise NotImplementedError("Repo FastMCP server setup stub. Implemented in Phase 2 & 3.")


def search_code(query: str, path_pattern: str | None = None) -> list[dict[str, Any]]:
    """Search code across the workspace using ripgrep with line numbers."""
    raise NotImplementedError("search_code tool stub. Implemented in Phase 2.")


def read_file(path: str, start_line: int | None = None, end_line: int | None = None) -> str:
    """Read file content within optional bounded line range."""
    raise NotImplementedError("read_file tool stub. Implemented in Phase 2.")


def list_symbols(path: str) -> list[dict[str, Any]]:
    """Extract AST-based symbol outline (functions, classes, signatures, line ranges)."""
    raise NotImplementedError("list_symbols tool stub. Implemented in Phase 2.")


def apply_patch(patch: str) -> dict[str, Any]:
    """Apply a unified diff patch to the worktree."""
    raise NotImplementedError("apply_patch tool stub. Implemented in Phase 3.")


def git_diff() -> str:
    """Return the current working tree git diff."""
    raise NotImplementedError("git_diff tool stub. Implemented in Phase 3.")
