"""Pydantic schemas for specialist agents and tool interactions.

Purpose: Defines real, strictly validated input and output contracts for each agent in the graph.
Phase: Phase 0 (Foundation).
Serves: Supervisor, Issue Analyst, Code Locator, Clarifier, Fixer, Reviewer, PR Writer.
"""

from typing import Literal

from pydantic import BaseModel, Field


class IssueAnalysis(BaseModel):
    """Output schema for Issue Analyst agent."""

    issue_id: str = Field(description="Issue identifier or number")
    title: str = Field(description="Issue title")
    expected_behavior: str = Field(description="Expected behavior extracted from issue description and comments")
    actual_behavior: str = Field(description="Current / erroneous behavior reported")
    reproduction_steps: list[str] = Field(default_factory=list, description="Extracted reproduction steps")
    stack_trace: str | None = Field(default=None, description="Extracted stack trace if present in issue")
    ambiguity_score: float = Field(ge=0.0, le=1.0, description="Ambiguity rating from 0.0 (crystal clear) to 1.0 (highly ambiguous)")
    suggested_clarification: str | None = Field(default=None, description="Candidate question if ambiguity is high")


class SymbolInfo(BaseModel):
    """AST-extracted symbol metadata."""

    name: str = Field(description="Symbol identifier name")
    kind: Literal["function", "class", "method"] = Field(description="Type of code symbol")
    line_start: int = Field(ge=1, description="Starting line number")
    line_end: int = Field(ge=1, description="Ending line number")
    signature: str = Field(description="Function or method argument signature")


class LocationResult(BaseModel):
    """Output schema for Code Locator agent."""

    relevant_files: list[str] = Field(description="Relative file paths identified as most likely containing the bug")
    candidate_symbols: list[SymbolInfo] = Field(default_factory=list, description="Target functions/classes identified by AST outline")
    search_queries_used: list[str] = Field(default_factory=list, description="Keywords/regex queries used during ripgrep search")
    rationale: str = Field(description="Explanation of why these locations were selected")


class ClarificationQuestion(BaseModel):
    """Clarification request schema sent to the developer."""

    question: str = Field(description="The single targeted question to ask the developer")
    options: list[str] = Field(default_factory=list, description="Optional multiple-choice alternatives if applicable")
    context_snippet: str | None = Field(default=None, description="Brief context code snippet explaining the question")


class ClarificationResult(BaseModel):
    """Output schema for Clarifier agent."""

    asked: bool = Field(description="Whether a question was posed to the developer")
    question: str | None = Field(default=None, description="Question asked if any")
    answer: str | None = Field(default=None, description="Developer response received via interrupt")
    resolved_ambiguity: bool = Field(default=False, description="Whether the developer answer resolved the ambiguity")


class PatchPlan(BaseModel):
    """Output schema for Fixer agent's initial plan."""

    target_files: list[str] = Field(description="Files to be edited")
    summary: str = Field(description="Summary of the intended bug fix")
    planned_steps: list[str] = Field(description="Step-by-step modification plan")
    risks: list[str] = Field(default_factory=list, description="Potential side-effects or regressions considered")


class TestExecutionResult(BaseModel):
    """Output schema for Test Runner (deterministic Docker sandbox)."""

    __test__ = False

    passed: bool = Field(description="Whether all tests and quality checks passed")
    exit_code: int = Field(description="Exit code returned by test runner")
    tests_run: int = Field(default=0, description="Total number of tests executed")
    tests_failed: int = Field(default=0, description="Number of failed tests")
    failed_test_names: list[str] = Field(default_factory=list, description="Identifiers of failing test cases")
    failure_type: Literal["none", "code_failure", "test_failure", "infra_failure", "timeout"] = Field(
        default="none", description="Classification of the failure"
    )
    stdout: str = Field(default="", description="Sanitized stdout from test run")
    stderr: str = Field(default="", description="Sanitized stderr from test run")


class ReviewResult(BaseModel):
    """Output schema for Reviewer agent."""

    approved: bool = Field(description="Whether the patch is approved for draft PR")
    test_tampering_detected: bool = Field(description="Whether the diff improperly modifies test assertions")
    unrelated_edits_detected: bool = Field(description="Whether the diff introduces unrelated changes or refactoring")
    regression_risk: Literal["low", "medium", "high"] = Field(description="Estimated regression risk")
    critique: str = Field(description="Detailed code review commentary and feedback")


class DraftPRResult(BaseModel):
    """Output schema for PR Writer agent."""

    pr_url: str = Field(description="URL of the opened draft pull request")
    branch_name: str = Field(description="Name of the pushed working branch")
    title: str = Field(description="Pull request title")
    body: str = Field(description="Structured pull request markdown body")
    is_draft: bool = Field(default=True, description="Always True; PR is never automatically merged or published")


class SupervisorDecision(BaseModel):
    """Output schema for Supervisor routing node."""

    next_agent: Literal["issue_analyst", "code_locator", "clarifier", "fixer", "test_runner", "reviewer", "pr_writer", "end"] = Field(
        description="Next specialist agent to invoke"
    )
    terminate: bool = Field(default=False, description="Whether workflow should stop immediately")
    reason: str = Field(description="Justification for routing decision or termination")
