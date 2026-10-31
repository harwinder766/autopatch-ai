# Clarify-or-Code

Clarify-or-Code is an issue-to-PR multi-agent system built with LangGraph, FastMCP, and LiteLLM that investigates a core software engineering research question:

> **Does asking a developer ONE clarifying question before writing code improve the resolve rate, and can a learned gate reliably predict when to ask?**

---

## Architecture

The system orchestrates a set of specialist agents using a **LangGraph supervisor graph** with shared typed state and Pydantic-validated transitions:

- **Supervisor**: Evaluates progress, enforces cost and retry caps, and directs transitions.
- **Issue Analyst**: Ingests issue details and comments via GitHub MCP; identifies expected vs. actual behaviors and ambiguity score.
- **Code Locator**: Navigates the repository using agentic search tools (ripgrep, ast-based symbols) to find target files and functions.
- **Clarifier**: Triggers an `interrupt()` to ask the human developer a single targeted question if ambiguity exceeds threshold.
- **Fixer**: Generates an actionable repair plan and unified diff edits via the repo MCP patch tool.
- **Test Runner**: Deterministic code (no LLM) that executes `pytest` and `ruff` inside a locked-down Docker sandbox.
- **Reviewer**: Audits the diff using an independent model (different from the Fixer) to detect unrelated changes, test tampering, or regressions.
- **PR Writer**: Composes a structured PR description and opens a draft pull request on a user-owned repository fork.

### MCP Permission Boundaries
All tool interactions occur across three isolated **FastMCP** servers using `langchain-mcp-adapters` with per-agent tool allowlists:
- **`repo_server`**: Code search, AST symbol extraction, file reading, and unified patch application on local git worktrees.
- **`sandbox_server`**: Runs tests inside a hardened Docker container (no network, read-only root, read-only tests, resource limits).
- **`github_server`**: Holds the scoped GitHub token to read issues and create draft PRs.

---

## Roadmap & Phases

- **Phase 0**: Foundation (Repository structure, state schemas, MCP stubs, CI, smoke tests) — *Current*
- **Phase 1**: Issue ingestion & git worktree setup
- **Phase 2**: Agentic code localization (AST + ripgrep)
- **Phase 3**: Patch generation & unified diff tooling
- **Phase 4**: Docker test execution & bounded repair loop (max 3 retries)
- **Phase 5**: Reviewer audit, draft PR creation, baseline validation on 10–15 issues (**End of MVP**)
- **Phase 6**: Benchmark task mining (40–60 tasks) & evaluation framework
- **Phase 7**: Advanced / hybrid retrieval (FAISS, tree-sitter chunking)
- **Phase 8**: Clarification gating (Rule-based & LightGBM/SHAP) and ablation study
- **Phase 9**: Voice clarification layer (Prisma STT, Timbre TTS, RapidFuzz)
- **Phase 10**: FastAPI service & Streamlit trace viewer

---

## Environment Setup

### Prerequisites
- Python 3.12+
- `uv` package manager (`pip install uv` or standalone installer)
- Git CLI
- Docker (for Phase 4+ sandbox execution)

### Installation
Clone the repository and install dependencies using `uv`:

```bash
# Clone the repository
git clone https://github.com/harwinder766/autopatch-ai.git
cd autopatch-ai

# Synchronize virtual environment with uv
uv sync

# Copy and configure environment variables
cp .env.example .env
```

### Running Tests and Linting
```bash
# Run test suite
uv run pytest

# Run code style and lint checks
uv run ruff check .
```

---

## Project Structure
```text
├── docs/                      # Architectural specs, phase roadmap, decisions
├── src/clarify_or_code/       # Core application package
│   ├── agents/               # Specialist agent definitions and Pydantic schemas
│   ├── clarification/        # Clarification gate (rule-based and ML gate)
│   ├── evaluation/           # Benchmark mining, test runners, and metrics
│   ├── graph/                # LangGraph state, workflow, nodes, and routing
│   ├── llm/                  # LiteLLM client, cost tracking, agent prompts
│   ├── mcp_servers/          # FastMCP servers (repo, sandbox, github)
│   ├── observability/        # Logging and token cost accounting
│   ├── repo/                 # Git worktree, ripgrep, AST symbols, patching
│   ├── sandbox/              # Docker execution and security policies
│   └── voice/                # STT/TTS voice layer stubs (Phase 9)
├── apps/                     # FastAPI and Streamlit interfaces (Phase 10)
├── benchmark/                # Mined evaluation dataset (tasks.jsonl)
├── docker/                   # Hardened sandbox Dockerfile & compose config
├── scripts/                  # Task set generation & benchmark runners
└── tests/                    # Unit and integration smoke tests
```
