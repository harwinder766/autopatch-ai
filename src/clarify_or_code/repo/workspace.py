"""Git repository caching and worktree isolation.

Purpose: Manages cached bare clones keyed by repo + commit SHA and creates disposable worktrees per task.
Phase: Phase 0 (Foundation stub), implemented in Phase 1.
Serves: repo FastMCP server and repository setup.
"""

from pathlib import Path


class WorkspaceManager:
    """Manages cached git repositories and dedicated worktrees per task."""

    def __init__(self, cache_dir: Path) -> None:
        self.cache_dir = cache_dir

    def ensure_cached_repo(self, repo_url: str, commit_sha: str) -> Path:
        """Clone or update bare repository cache for a given commit SHA."""
        raise NotImplementedError("Repo caching stub. Implemented in Phase 1.")

    def create_worktree(self, repo_url: str, commit_sha: str, task_id: str) -> Path:
        """Create an isolated git worktree for a specific benchmark task or issue."""
        raise NotImplementedError("Worktree creation stub. Implemented in Phase 1.")

    def cleanup_worktree(self, worktree_path: Path) -> None:
        """Prune and remove a disposable git worktree."""
        raise NotImplementedError("Worktree cleanup stub. Implemented in Phase 1.")
