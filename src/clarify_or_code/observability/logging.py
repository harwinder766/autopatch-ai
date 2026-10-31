"""Structured logging and MCP tool call audit recording.

Purpose: Records caller, arguments, and sanitized outputs for every MCP tool invocation and agent action.
Phase: Phase 0 (Foundation stub), implemented in Phase 1.
Serves: Entire multi-agent system and security audit.
"""

from typing import Any


def log_tool_call(caller: str, tool_name: str, arguments: dict[str, Any], result: Any) -> None:
    """Record structured log entry for an MCP tool call."""
    raise NotImplementedError("Tool call logging stub. Implemented in Phase 1.")


def log_agent_event(agent_name: str, event_type: str, payload: dict[str, Any]) -> None:
    """Record agent state transition or decision event."""
    raise NotImplementedError("Agent event logging stub. Implemented in Phase 1.")
