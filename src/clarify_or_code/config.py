"""Configuration management for Clarify-or-Code.

Purpose: Loads and validates environment variables, model tiers, cost caps, and sandbox rules.
Phase: Phase 0 (Foundation).
Serves: System-wide configuration.
"""

from pydantic import BaseModel, Field


class Settings(BaseModel):
    """Runtime configuration loaded from environment variables."""

    # GitHub
    github_token: str = Field(default="", description="Scoped GitHub access token")
    github_owner: str = Field(default="", description="Target GitHub account or organization")
    github_default_fork: str = Field(default="", description="Target fork repo owned by user")

    # LLM Models
    model_strong: str = Field(default="anthropic/claude-3-5-sonnet-20241022", description="Strong code model")
    model_cheap: str = Field(default="anthropic/claude-3-5-haiku-20241022", description="Cheap reasoning model")
    model_reviewer: str = Field(default="openai/gpt-4o-mini", description="Independent reviewer model")

    # Cost Limits
    hard_cost_cap_per_run: float = Field(default=2.50, description="Maximum budget in USD per task run")

    # Sandbox
    docker_image_name: str = Field(default="clarify-or-code-sandbox:latest", description="Sandbox Docker image")
    sandbox_timeout_seconds: int = Field(default=180, description="Test execution timeout in seconds")
    sandbox_max_memory: str = Field(default="2g", description="Sandbox memory limit")
    sandbox_max_cpus: float = Field(default=2.0, description="Sandbox CPU quota")
    sandbox_max_pids: int = Field(default=100, description="Sandbox maximum process count")

    # Checkpoint
    checkpoint_db_path: str = Field(default="./checkpoints.sqlite", description="SQLite checkpointer database path")


def load_settings() -> Settings:
    """Load settings from environment."""
    return Settings()
