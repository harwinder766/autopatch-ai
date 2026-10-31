"""Benchmark execution runner and ablation driver.

Purpose: Executes benchmark tasks across ablation arms (never-ask, always-ask, rule-based, learned gate; single vs multi-agent; retry on/off).
Phase: Phase 0 (Foundation stub), implemented in Phase 6 and 8.
Serves: Benchmark evaluation framework.
"""

from pathlib import Path
from typing import Any

from clarify_or_code.evaluation.tasks import BenchmarkTask


class BenchmarkRunner:
    """Runs Clarify-or-Code evaluation across mined repository tasks."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir

    def run_task(self, task: BenchmarkTask, arm: str) -> dict[str, Any]:
        """Execute a single benchmark task under a specific experimental arm."""
        raise NotImplementedError("Benchmark task execution stub. Implemented in Phase 6 & 8.")

    def run_suite(self, tasks: list[BenchmarkTask], arms: list[str]) -> list[dict[str, Any]]:
        """Run benchmark suite across multiple experimental arms."""
        raise NotImplementedError("Benchmark suite execution stub. Implemented in Phase 6 & 8.")
