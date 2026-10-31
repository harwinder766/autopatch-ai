"""MCP client integration with per-agent tool allowlists.

Purpose: Manages MultiServerMCPClient connections to repo, sandbox, and github MCP servers, enforcing strict tool allowlists.
Phase: Phase 0 (Foundation stub), implemented in Phase 1.
Serves: All agents requiring MCP tool access.
"""

from typing import Any

AGENT_TOOL_ALLOWLISTS: dict[str, list[str]] = {
    "supervisor": [],
    "issue_analyst": ["get_issue", "list_comments"],
    "code_locator": ["search_code", "read_file", "list_symbols"],
    "clarifier": [],
    "fixer": ["read_file", "apply_patch", "git_diff"],
    "test_runner": ["run_tests", "run_lint", "get_logs"],
    "reviewer": ["read_file", "git_diff", "run_lint"],
    "pr_writer": ["create_branch", "push_branch", "open_draft_pr"],
}


class MCPClientManager:
    """Manages connections to FastMCP servers and provides filtered toolsets per agent."""

    def __init__(self, server_configs: dict[str, Any] | None = None) -> None:
        self.server_configs = server_configs or {}

    def get_tools_for_agent(self, agent_name: str) -> list[Any]:
        """Return allowed MCP tools for a specific agent based on AGENT_TOOL_ALLOWLISTS.

        Args:
            agent_name: Name of the specialist agent.

        Returns:
            List of LangChain-compatible tool callables.
        """
        raise NotImplementedError("MCP tool loading with per-agent allowlists stub. Implemented in Phase 1.")
