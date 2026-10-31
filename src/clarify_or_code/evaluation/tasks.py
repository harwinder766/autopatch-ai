"""Benchmark task definition and mining dataset loader.

Purpose: Loads and represents bug-fix tasks mined from real Python repositories.
Phase: Phase 0 (Foundation stub), implemented in Phase 6.
Serves: Benchmark evaluation framework.
"""

from pathlib import Path

from pydantic import BaseModel, Field


class BenchmarkTask(BaseModel):
    """Schema for a single bug-fix benchmark evaluation instance."""

    task_id: str = Field(description="Unique task identifier, e.g. 'pallets-click-1234'")
    repo_url: str = Field(description="Target repository GitHub URL")
    base_commit: str = Field(description="Commit SHA before the fix")
    issue_url: str = Field(description="URL to original GitHub issue")
    issue_text: str = Field(description="Concealed issue title and body")
    test_patch: str = Field(description="Ground truth test patch (concealed during evaluation)")
    ground_truth_patch: str = Field(description="Ground truth fix patch (concealed during evaluation)")


def load_tasks(tasks_path: Path) -> list[BenchmarkTask]:
    """Load evaluation tasks from tasks.jsonl file."""
    raise NotImplementedError("Benchmark task loader stub. Implemented in Phase 6.")
