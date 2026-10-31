"""Conditional routing logic for the LangGraph workflow.

Purpose: Determines edge transitions, retry counting (max 3), test outcome evaluation, and termination.
Phase: Phase 0 (Foundation stub), implemented in Phase 1 & 4.
Serves: Supervisor agent and conditional edges.
"""

from clarify_or_code.graph.state import AgentState


def route_next(state: AgentState) -> str:
    """Determine the next node based on supervisor decision and state flags."""
    raise NotImplementedError("Workflow edge routing stub. Implemented in Phase 1.")


def should_retry(state: AgentState) -> bool:
    """Check whether test failure qualifies for a repair attempt within the max 3 limit."""
    raise NotImplementedError("Retry decision stub. Implemented in Phase 4.")
