"""Sandbox isolation and security execution policies.

Purpose: Enforces container hardening rules: read-only root, read-only tests, no network, non-root user, resource bounds.
Phase: Phase 0 (Foundation).
Serves: docker_runner and sandbox MCP server.
"""

from pydantic import BaseModel, Field


class SandboxPolicy(BaseModel):
    """Execution constraints enforced on every container run."""

    network_disabled: bool = Field(default=True, description="Enforce --network none")
    run_as_non_root: bool = Field(default=True, description="Execute as non-root unprivileged user")
    read_only_root_fs: bool = Field(default=True, description="Mount root filesystem as read-only")
    mount_tests_read_only: bool = Field(default=True, description="Mount test directory as read-only to prevent tampering")
    no_docker_socket: bool = Field(default=True, description="Forbid mounting /var/run/docker.sock")
    no_host_mounts: bool = Field(default=True, description="Forbid arbitrary host filesystem mounts")
    strip_tokens_from_env: bool = Field(default=True, description="Strip GITHUB_TOKEN and API keys from container environment")

    # Resource Limits
    cpu_limit: float = Field(default=2.0, description="Maximum CPUs allocated")
    memory_limit: str = Field(default="2g", description="Maximum RAM allocated")
    pids_limit: int = Field(default=100, description="Maximum processes allowed")
    timeout_seconds: int = Field(default=180, description="Hard timeout for execution")
