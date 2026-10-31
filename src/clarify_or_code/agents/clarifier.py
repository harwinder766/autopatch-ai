"""Clarifier agent implementation.

Purpose: Formulates a single clarifying question and pauses execution via interrupt() when ambiguity is high.
Phase: Phase 0 (Foundation stub), fully implemented in Phase 8 (with rule-based gate integration).
Serves: Clarification interrupt node.
"""

from typing import Any

from clarify_or_code.agents.schemas import (
    ClarificationQuestion,
    ClarificationResult,
    IssueAnalysis,
    LocationResult,
)


class ClarifierAgent:
    """Specialist agent that drafts targeted clarifying questions before code generation."""

    def __init__(self, model_name: str, tools: list[Any] | None = None) -> None:
        self.model_name = model_name
        self.tools = tools or []

    def should_clarify(self, analysis: IssueAnalysis, location: LocationResult) -> bool:
        """Evaluate whether clarification is needed based on gating policy."""
        raise NotImplementedError("Clarification gating check stub. Implemented in Phase 8.")

    def draft_question(self, analysis: IssueAnalysis, location: LocationResult) -> ClarificationQuestion:
        """Formulate a single precise clarifying question for the developer."""
        raise NotImplementedError("Clarification question generation stub. Implemented in Phase 8.")

    def process_answer(self, question: ClarificationQuestion, answer: str) -> ClarificationResult:
        """Integrate developer response into workflow state."""
        raise NotImplementedError("Clarification response processing stub. Implemented in Phase 8.")
