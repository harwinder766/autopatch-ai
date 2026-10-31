"""FastMCP GitHub tools server.

Purpose: Handles privileged GitHub operations using a scoped token; never merges branches.
Phase: Phase 0 (Foundation stub), implemented in Phases 1 and 5.
Serves: Issue Analyst and PR Writer agents.
"""

from typing import Any


def create_github_mcp_server(github_token: str) -> Any:
    """Create and configure the FastMCP GitHub server instance.

    Tools exposed:
    - get_issue(issue_url: str)
    - list_comments(issue_url: str)
    - create_branch(repo_url: str, branch_name: str, base_sha: str)
    - push_branch(repo_url: str, branch_name: str)
    - open_draft_pr(repo_url: str, branch_name: str, title: str, body: str)
    """
    raise NotImplementedError("GitHub FastMCP server setup stub. Implemented in Phase 1 & 5.")


def get_issue(issue_url: str) -> dict[str, Any]:
    """Fetch issue metadata, title, and body from GitHub."""
    raise NotImplementedError("get_issue tool stub. Implemented in Phase 1.")


def list_comments(issue_url: str) -> list[dict[str, Any]]:
    """Fetch comments associated with a GitHub issue."""
    raise NotImplementedError("list_comments tool stub. Implemented in Phase 1.")


def create_branch(repo_url: str, branch_name: str, base_sha: str) -> dict[str, Any]:
    """Create a new working branch in the repository fork."""
    raise NotImplementedError("create_branch tool stub. Implemented in Phase 1.")


def push_branch(repo_url: str, branch_name: str) -> dict[str, Any]:
    """Push local branch commits to the remote fork."""
    raise NotImplementedError("push_branch tool stub. Implemented in Phase 5.")


def open_draft_pr(repo_url: str, branch_name: str, title: str, body: str) -> dict[str, Any]:
    """Open a DRAFT pull request against the base repository."""
    raise NotImplementedError("open_draft_pr tool stub. Implemented in Phase 5.")
