"""Supervisor agent implementation.

Purpose: Inspects shared graph state, caps retries (max 3), enforces cost budget, and orchestrates next steps.
Phase: Phase 0 (Foundation stub), implemented in Phase 1.
Serves: LangGraph supervisor coordinator.
"""

from clarify_or_code.agents.schemas import SupervisorDecision
from clarify_or_code.graph.state import AgentState


class SupervisorAgent:
    """Orchestrates specialist agents and enforces execution boundaries."""

    def __init__(self, model_name: str, cost_cap_usd: float = 2.50) -> None:
        self.model_name = model_name
        self.cost_cap_usd = cost_cap_usd

    def decide_next(self, state: AgentState) -> SupervisorDecision:
        """Evaluate graph state and return next agent routing decision."""
        raise NotImplementedError("Supervisor decision logic stub. Implemented in Phase 1.")
