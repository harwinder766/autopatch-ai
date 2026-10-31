"""Benchmark reporting and table generator.

Purpose: Formats ablation comparison tables and markdown reports for evaluation results.
Phase: Phase 0 (Foundation stub), implemented in Phase 6.
Serves: Benchmark evaluation framework.
"""

from pathlib import Path

from clarify_or_code.evaluation.metrics import EvaluationMetrics


def generate_markdown_report(metrics_by_arm: dict[str, EvaluationMetrics], output_path: Path) -> str:
    """Generate markdown summary table comparing arms (never-ask, always-ask, rule-based, learned gate)."""
    raise NotImplementedError("Benchmark report generator stub. Implemented in Phase 6.")
