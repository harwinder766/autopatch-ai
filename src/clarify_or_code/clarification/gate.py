"""Clarification decision gate.

Purpose: Decides whether to ask a clarifying question before coding (rule-based first, learned gate in Phase 8).
Phase: Phase 0 (Foundation stub), rule-based in Phase 0/5, LightGBM in Phase 8.
Serves: Clarifier agent and graph routing edge.
"""

from clarify_or_code.agents.schemas import IssueAnalysis, LocationResult


class ClarificationGate:
    """Evaluates whether the system should interrupt for developer clarification."""

    def __init__(self, mode: str = "rule_based") -> None:
        self.mode = mode

    def should_ask(
        self,
        analysis: IssueAnalysis,
        location: LocationResult,
    ) -> bool:
        """Determine if clarification is required before coding.

        Policy modes supported across phases:
        - 'never': Always returns False.
        - 'always': Always returns True.
        - 'rule_based': Threshold on ambiguity score and missing stack traces.
        - 'learned': Evaluates trained LightGBM model.
        """
        raise NotImplementedError("Clarification gate evaluation stub. Rule-based implemented in Phase 5, learned in Phase 8.")
