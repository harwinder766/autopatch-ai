"""Docker execution sandbox and security policies.

Purpose: Manages isolated, hardened container execution for pytest and ruff.
Phase: Phase 0 (Foundation).
Serves: sandbox FastMCP server and deterministic Test Runner.
"""

__all__ = ["docker_runner", "policies"]
