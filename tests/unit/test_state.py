"""Unit tests for LangGraph AgentState model."""

from clarify_or_code.agents.schemas import (
    IssueAnalysis,
    ReviewResult,
    TestExecutionResult,
)
from clarify_or_code.graph.state import AgentState


def test_agent_state_defaults() -> None:
    """Test initial default values of AgentState."""
    state = AgentState(
        issue_url="https://github.com/pallets/click/issues/123",
        repo_url="https://github.com/pallets/click",
    )
    assert state.issue_url == "https://github.com/pallets/click/issues/123"
    assert state.status == "pending"
    assert state.retry_count == 0
    assert state.total_cost_usd == 0.0
    assert state.analysis is None
    assert state.patch == ""
    assert state.relevant_files == []


def test_agent_state_full_lifecycle() -> None:
    """Test updating state through lifecycle steps."""
    state = AgentState(
        issue_url="https://github.com/pallets/click/issues/123",
        repo_url="https://github.com/pallets/click",
        workspace_path="/tmp/workspaces/task-1",
        analysis=IssueAnalysis(
            issue_id="123",
            title="Crash on flag",
            expected_behavior="Return 0",
            actual_behavior="Exit 1",
            ambiguity_score=0.1,
        ),
        relevant_files=["src/click/core.py"],
        patch="--- a/src/click/core.py\n+++ b/src/click/core.py\n@@ ...",
        test_results=TestExecutionResult(
            passed=True,
            exit_code=0,
            tests_run=50,
            tests_failed=0,
        ),
        retry_count=1,
        review_result=ReviewResult(
            approved=True,
            test_tampering_detected=False,
            unrelated_edits_detected=False,
            regression_risk="low",
            critique="Looks solid",
        ),
        pr_url="https://github.com/pallets/click/pull/999",
        status="resolved",
    )
    assert state.status == "resolved"
    assert state.retry_count == 1
    assert state.review_result.approved is True
    assert state.test_results.passed is True
