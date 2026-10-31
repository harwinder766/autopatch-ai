"""FastMCP sandbox tools server.

Purpose: Manages hardened Docker containers for test execution and linting without network access.
Phase: Phase 0 (Foundation stub), implemented in Phase 4.
Serves: Test Runner (deterministic node) and Reviewer agent.
"""

from typing import Any


def create_sandbox_mcp_server() -> Any:
    """Create and configure the FastMCP sandbox server instance.

    Tools exposed:
    - run_tests(test_target: str | None)
    - run_lint(path: str | None)
    - get_logs(run_id: str)
    """
    raise NotImplementedError("Sandbox FastMCP server setup stub. Implemented in Phase 4.")


def run_tests(test_target: str | None = None) -> dict[str, Any]:
    """Execute pytest inside the hardened sandbox container with network disabled."""
    raise NotImplementedError("run_tests tool stub. Implemented in Phase 4.")


def run_lint(path: str | None = None) -> dict[str, Any]:
    """Run ruff linter inside the sandbox container."""
    raise NotImplementedError("run_lint tool stub. Implemented in Phase 4.")


def get_logs(run_id: str) -> str:
    """Retrieve full execution stdout and stderr for a test run."""
    raise NotImplementedError("get_logs tool stub. Implemented in Phase 4.")
