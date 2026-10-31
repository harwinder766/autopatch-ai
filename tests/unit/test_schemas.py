"""Unit tests for agent output Pydantic schemas."""

import pytest
from pydantic import ValidationError

from clarify_or_code.agents.schemas import (
    ClarificationQuestion,
    ClarificationResult,
    DraftPRResult,
    IssueAnalysis,
    LocationResult,
    PatchPlan,
    ReviewResult,
    SupervisorDecision,
    SymbolInfo,
    TestExecutionResult,
)


def test_issue_analysis_schema_valid() -> None:
    """Test valid IssueAnalysis model creation."""
    analysis = IssueAnalysis(
        issue_id="42",
        title="Fix null pointer exception in parser",
        expected_behavior="Parser handles None gracefully",
        actual_behavior="Raises TypeError on None",
        ambiguity_score=0.2,
    )
    assert analysis.issue_id == "42"
    assert analysis.ambiguity_score == 0.2
    assert analysis.reproduction_steps == []


def test_issue_analysis_ambiguity_bounds() -> None:
    """Test that ambiguity score must be between 0.0 and 1.0."""
    with pytest.raises(ValidationError):
        IssueAnalysis(
            issue_id="1",
            title="Title",
            expected_behavior="Expected",
            actual_behavior="Actual",
            ambiguity_score=1.5,
        )


def test_location_result_schema() -> None:
    """Test valid LocationResult schema."""
    loc = LocationResult(
        relevant_files=["src/parser.py"],
        candidate_symbols=[
            SymbolInfo(
                name="parse_token",
                kind="function",
                line_start=10,
                line_end=25,
                signature="def parse_token(val: str | None) -> Token:",
            )
        ],
        rationale="Error trace points to line 15 in parse_token",
    )
    assert len(loc.relevant_files) == 1
    assert loc.candidate_symbols[0].name == "parse_token"


def test_clarification_schemas() -> None:
    """Test ClarificationQuestion and ClarificationResult."""
    q = ClarificationQuestion(
        question="Should None return an EmptyToken or raise ValueError?",
        options=["Return EmptyToken", "Raise ValueError"],
    )
    assert len(q.options) == 2

    res = ClarificationResult(
        asked=True,
        question=q.question,
        answer="Return EmptyToken",
        resolved_ambiguity=True,
    )
    assert res.asked is True
    assert res.resolved_ambiguity is True


def test_patch_plan_schema() -> None:
    """Test PatchPlan schema."""
    plan = PatchPlan(
        target_files=["src/parser.py"],
        summary="Add check for None input before token lookup",
        planned_steps=["Inspect token", "Return EmptyToken if None"],
    )
    assert plan.target_files == ["src/parser.py"]


def test_test_execution_result_schema() -> None:
    """Test TestExecutionResult schema."""
    test_res = TestExecutionResult(
        passed=True,
        exit_code=0,
        tests_run=12,
        tests_failed=0,
    )
    assert test_res.passed is True
    assert test_res.failure_type == "none"


def test_review_result_schema() -> None:
    """Test ReviewResult schema."""
    rev = ReviewResult(
        approved=True,
        test_tampering_detected=False,
        unrelated_edits_detected=False,
        regression_risk="low",
        critique="Clean minimal fix adhering strictly to the bug scope.",
    )
    assert rev.approved is True


def test_draft_pr_result_schema() -> None:
    """Test DraftPRResult schema."""
    pr = DraftPRResult(
        pr_url="https://github.com/harwinder766/autopatch-ai/pull/1",
        branch_name="fix/parser-none-handling",
        title="fix: handle None input in parse_token",
        body="## Summary\nHandles None gracefully.",
    )
    assert pr.is_draft is True
    assert "pull/1" in pr.pr_url


def test_supervisor_decision_schema() -> None:
    """Test SupervisorDecision schema."""
    decision = SupervisorDecision(
        next_agent="issue_analyst",
        terminate=False,
        reason="Initial issue ingestion",
    )
    assert decision.next_agent == "issue_analyst"
