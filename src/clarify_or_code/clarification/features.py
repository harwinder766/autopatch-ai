"""Feature extraction for clarification gating.

Purpose: Extracts signals (issue length, presence of stack traces, retrieval score spread, symbol count) to predict failure risk.
Phase: Phase 0 (Foundation stub), implemented in Phase 8.
Serves: Clarification gate (rule-based and LightGBM model).
"""

from clarify_or_code.agents.schemas import IssueAnalysis, LocationResult


class ClarificationFeatures:
    """Feature vector representation used by the clarification gate."""

    @classmethod
    def extract_features(
        cls,
        analysis: IssueAnalysis,
        location: LocationResult,
    ) -> dict[str, float | int | bool]:
        """Extract numeric and categorical signals from issue and location state."""
        raise NotImplementedError("Clarification feature extraction stub. Implemented in Phase 8.")
