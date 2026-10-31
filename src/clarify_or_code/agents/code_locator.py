"""Code Locator agent implementation.

Purpose: Navigates repository using agentic search (ripgrep, ast symbols) to identify candidate bug locations.
Phase: Phase 0 (Foundation stub), implemented in Phase 2.
Serves: Code localization node (calls repo MCP server tools).
"""

from typing import Any

from clarify_or_code.agents.schemas import IssueAnalysis, LocationResult


class CodeLocatorAgent:
    """Specialist agent that conducts agentic code search without vector databases."""

    def __init__(self, model_name: str, tools: list[Any] | None = None) -> None:
        self.model_name = model_name
        self.tools = tools or []

    def locate(self, analysis: IssueAnalysis) -> LocationResult:
        """Search codebase via repo MCP server and return targeted files and symbols."""
        raise NotImplementedError("Code Locator execution stub. Implemented in Phase 2.")
