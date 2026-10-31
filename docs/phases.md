# Project Phases & Roadmap

This document outlines Phases 0 through 10 of the Clarify-or-Code roadmap.
**The Minimum Viable Product (MVP) ends at the completion of Phase 5.**

- [x] **Phase 0: Foundation** *(Current Phase - Scaffolding)*
  - [x] Set up repository structure, `uv` environment, and dependency configuration (`pyproject.toml`).
  - [x] Define typed LangGraph state schema (`AgentState`) and Pydantic agent schemas (`agents/schemas.py`).
  - [x] Create MCP server stubs (`repo_server`, `sandbox_server`, `github_server`) and client allowlist scaffolding.
  - [x] Establish linting (`ruff`), testing (`pytest`), CI pipeline (`.github/workflows/ci.yml`), and smoke tests.

- [ ] **Phase 1: Issue Ingestion & Repository Setup**
  - [ ] Accept issue URL, parse owner, repo, and issue number.
  - [ ] Fetch title, body, and comments via `github` MCP server.
  - [ ] Clone repository into cached bare/mirror directory by commit SHA.
  - [ ] Create isolated git worktree per task and checkout target branch.

- [ ] **Phase 2: Code Localization**
  - [ ] Scan repo excluding junk/build directories.
  - [ ] AST symbol extraction (`list_symbols`) for functions and classes.
  - [ ] Agentic ripgrep search (`search_code`) with line numbers and bounding.
  - [ ] Produce bounded context package for downstream LLM agents.

- [ ] **Phase 3: Patch Generation**
  - [ ] Fixer agent writes short plan and unified diff edits.
  - [ ] Apply edits safely via `repo` MCP server (`apply_patch`).
  - [ ] Validate diff using `git_diff` tool.

- [ ] **Phase 4: Docker Testing & Repair Loop**
  - [ ] Build locked-down Docker image with pre-installed dependencies.
  - [ ] Run pytest in container with network disabled, non-root user, memory/CPU limits, and read-only test mounts.
  - [ ] Parse test failures and feed error traces back to Fixer agent.
  - [ ] Enforce bounded retry loop (maximum 3 repair attempts).

- [ ] **Phase 5: Draft PR & Baseline Run (End of MVP)**
  - [ ] Integrate Reviewer agent (runs independent model to check diff for regressions and tampering).
  - [ ] Integrate PR Writer agent to draft structured PR descriptions.
  - [ ] Push working branch and open draft PR on user-owned fork via `github` MCP server.
  - [ ] Conduct baseline sanity check on 10 to 15 resolved issues.

---
### Post-MVP Phases

- [ ] **Phase 6: Benchmark Mining & Evaluation**
  - [ ] Mine 40 to 60 bug-fix tasks from 5 to 8 small Python repositories using PyDriller.
  - [ ] Record ground-truth patches and tests while concealing them during benchmark runs.
  - [ ] Implement evaluation harness tracking resolve rate, first-attempt success, repair success, and cost per run.

- [ ] **Phase 7: Advanced / Hybrid Retrieval**
  - [ ] Implement tree-sitter chunking and syntax navigation.
  - [ ] Add vector ranking / embeddings with FAISS and hybrid BM25 integration.
  - [ ] Evaluate Recall@5 and Recall@10 against baseline agentic ripgrep.

- [ ] **Phase 8: Clarification Gate & Ablation Study**
  - [ ] Implement LangGraph `interrupt()` in Clarifier node to pause for developer input.
  - [ ] Train learned gate (LightGBM on features like retrieval gap, issue length, stack trace presence) with SHAP explanations.
  - [ ] Run 4-arm ablation: never-ask, always-ask, rule-based ask, learned gate.
  - [ ] Run architecture ablations: single-agent vs multi-agent, retry on/off, with/without reviewer.

- [ ] **Phase 9: Voice Layer**
  - [ ] Integrate Prisma streaming STT for spoken clarification in developer vernacular.
  - [ ] Integrate Timbre TTS for synthesized audio prompts.
  - [ ] Snap spoken identifier misspellings to real codebase symbols using `rapidfuzz`.

- [ ] **Phase 10: Service & Web Interface**
  - [ ] Develop FastAPI service endpoint for triggering issue remediation pipelines.
  - [ ] Build Streamlit UI showing live LangGraph execution trace and state inspection.
  - [ ] Expose outer MCP server allowing Claude Desktop or IDEs to submit issues directly.
