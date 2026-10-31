# Locked-down Docker Sandbox for Clarify-or-Code Test Execution
# Purpose: Pre-builds dependencies and provides hardened runtime environment.
# Phase: Phase 4 (Docker testing and repair loop).

FROM python:3.12-slim-bookworm

# Install base system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast, reproducible dependency resolution
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create unprivileged sandbox user
RUN useradd -m -u 1000 -s /bin/bash sandboxuser

# Set working directory
WORKDIR /workspace

# Set default user to unprivileged non-root user
USER sandboxuser

# Environment flags: enforce non-interactive, isolated execution
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Default entrypoint for test execution
ENTRYPOINT ["pytest"]
CMD ["-v"]
