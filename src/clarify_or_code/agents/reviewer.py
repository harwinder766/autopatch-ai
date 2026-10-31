"""Reviewer agent implementation.

Purpose: Audits diffs using an independent model to detect regressions, test tampering, or unrelated edits.
Phase: Phase 0 (Foundation stub), implemented in Phase 5.
Serves: Diff review node (calls repo read-only MCP tools and sandbox linter).
"""

from typing import Any

from clarify_or_code.agents.schemas import IssueAnalysis, ReviewResult


class ReviewerAgent:
    """Specialist agent running an independent model to review generated diffs."""

    def __init__(self, model_name: str, tools: list[Any] | None = None) -> None:
        self.model_name = model_name
        self.tools = tools or []

    def review(self, patch: str, analysis: IssueAnalysis) -> ReviewResult:
        """Audit the patch against original issue for test tampering and regressions."""
        raise NotImplementedError("Reviewer execution stub. Implemented in Phase 5.")
