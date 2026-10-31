"""Smoke test verifying every package and module in clarify_or_code can be imported cleanly."""

import importlib

import pytest

MODULES_TO_IMPORT = [
    # Root
    "clarify_or_code",
    "clarify_or_code.config",
    "clarify_or_code.cli",
    # Graph
    "clarify_or_code.graph",
    "clarify_or_code.graph.state",
    "clarify_or_code.graph.workflow",
    "clarify_or_code.graph.nodes",
    "clarify_or_code.graph.routing",
    # Agents
    "clarify_or_code.agents",
    "clarify_or_code.agents.schemas",
    "clarify_or_code.agents.supervisor",
    "clarify_or_code.agents.issue_analyst",
    "clarify_or_code.agents.code_locator",
    "clarify_or_code.agents.clarifier",
    "clarify_or_code.agents.fixer",
    "clarify_or_code.agents.reviewer",
    "clarify_or_code.agents.pr_writer",
    # LLM
    "clarify_or_code.llm",
    "clarify_or_code.llm.client",
    # MCP Servers & Client
    "clarify_or_code.mcp_servers",
    "clarify_or_code.mcp_servers.repo_server",
    "clarify_or_code.mcp_servers.sandbox_server",
    "clarify_or_code.mcp_servers.github_server",
    "clarify_or_code.mcp_client",
    # Repo tools
    "clarify_or_code.repo",
    "clarify_or_code.repo.workspace",
    "clarify_or_code.repo.search",
    "clarify_or_code.repo.symbols",
    "clarify_or_code.repo.patching",
    # Sandbox
    "clarify_or_code.sandbox",
    "clarify_or_code.sandbox.docker_runner",
    "clarify_or_code.sandbox.policies",
    # Clarification
    "clarify_or_code.clarification",
    "clarify_or_code.clarification.gate",
    "clarify_or_code.clarification.features",
    # Evaluation
    "clarify_or_code.evaluation",
    "clarify_or_code.evaluation.tasks",
    "clarify_or_code.evaluation.runner",
    "clarify_or_code.evaluation.metrics",
    "clarify_or_code.evaluation.report",
    # Voice stubs
    "clarify_or_code.voice",
    "clarify_or_code.voice.stt",
    "clarify_or_code.voice.tts",
    # Observability
    "clarify_or_code.observability",
    "clarify_or_code.observability.logging",
    "clarify_or_code.observability.cost",
]


@pytest.mark.parametrize("module_name", MODULES_TO_IMPORT)
def test_import_module(module_name: str) -> None:
    """Verify that each module imports cleanly without import errors or side effects."""
    mod = importlib.import_module(module_name)
    assert mod is not None
    assert hasattr(mod, "__doc__")
    assert mod.__doc__ is not None
    assert len(mod.__doc__.strip()) > 0
