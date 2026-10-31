"""Docker sandbox runner for executing pytest and ruff.

Purpose: Spawns and manages hardened, ephemeral containers enforcing SandboxPolicy.
Phase: Phase 0 (Foundation stub), implemented in Phase 4.
Serves: sandbox FastMCP server and deterministic Test Runner.
"""

from pathlib import Path

from clarify_or_code.agents.schemas import TestExecutionResult
from clarify_or_code.sandbox.policies import SandboxPolicy


class DockerRunner:
    """Interacts with Docker daemon to run test suites under strict isolation policies."""

    def __init__(self, policy: SandboxPolicy | None = None) -> None:
        self.policy = policy or SandboxPolicy()

    def build_task_image(self, repo_dir: Path, image_tag: str) -> None:
        """Pre-build environment image with all dependencies installed."""
        raise NotImplementedError("Docker environment build stub. Implemented in Phase 4.")

    def run_pytest(
        self,
        image_tag: str,
        worktree_path: Path,
        test_file: str | None = None,
    ) -> TestExecutionResult:
        """Run pytest inside isolated container with network disabled and test files mounted read-only."""
        raise NotImplementedError("Docker test execution stub. Implemented in Phase 4.")

    def run_ruff(self, image_tag: str, worktree_path: Path) -> dict:
        """Execute ruff linter inside the sandbox container."""
        raise NotImplementedError("Docker lint execution stub. Implemented in Phase 4.")
