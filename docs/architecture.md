# Clarify-or-Code Architecture

## Overview
Clarify-or-Code is a stateful multi-agent system designed to ingest a GitHub issue, locate relevant code, determine whether clarification is needed, produce a patch, validate that patch within a locked-down Docker sandbox across a bounded retry loop, review the diff with an independent model, and open a draft pull request on a user-owned fork.

---

## Agent Roster

| Agent | Role / Job | Model Tier | Tools (via MCP) | Output Schema |
|---|---|---|---|---|
| **Supervisor** | Orchestrates graph execution, evaluates termination conditions, enforces cost & retry budgets | Cheap (e.g. Haiku) | Reads graph state only (no external tools) | `SupervisorDecision` |
| **Issue Analyst** | Parses issue title, body, and comments; extracts expected vs. actual behavior; computes ambiguity score | Cheap (e.g. Haiku) | GitHub read tools (`get_issue`, `list_comments`) | `IssueAnalysis` |
| **Code Locator** | Locates candidate files and symbols likely causing the bug using agentic search (ripgrep, ast symbols) | Cheap (e.g. Haiku) | Repo search & read tools (`search_code`, `read_file`, `list_symbols`) | `LocationResult` |
| **Clarifier** | Triggers LangGraph `interrupt()` when ambiguity/risk exceeds gate threshold to solicit human clarification | Cheap (e.g. Haiku) | Graph interrupt interface (`interrupt()`) | `ClarificationResult` |
| **Fixer** | Formulates repair plan, writes unified diff / edits, iterates based on test failure feedback | Strong (e.g. Sonnet) | Repo read & patch tools (`read_file`, `apply_patch`, `git_diff`) | `PatchPlan` |
| **Test Runner** | Executes test suite and linter inside hardened Docker container. *(Plain deterministic code, NOT an LLM)* | None (No LLM) | Sandbox tools (`run_tests`, `run_lint`, `get_logs`) | `TestExecutionResult` |
| **Reviewer** | Audits diff against original issue for unrelated edits, regression risks, and test tampering. Uses a different model from Fixer | Independent (e.g. GPT-4o-mini) | Repo read-only tools, linter (`read_file`, `git_diff`, `run_lint`) | `ReviewResult` |
| **PR Writer** | Drafts comprehensive PR summary (issue reference, changes made, test output, notes) and opens draft PR | Cheap (e.g. Haiku) | GitHub write tools (`create_branch`, `push_branch`, `open_draft_pr`) | `DraftPRResult` |

---

## MCP Server Boundaries

Privileged operations are divided strictly across three FastMCP servers:

```
+-----------------------------------------------------------------------------------+
|                                 LangGraph Supervisor                              |
+-----------------------------------------------------------------------------------+
       |                        |                         |                  |
       v                        v                         v                  v
+---------------+      +------------------+      +------------------+  +-------------+
| Issue Analyst |      |   Code Locator   |      |      Fixer       |  |  PR Writer  |
+---------------+      +------------------+      +------------------+  +-------------+
       |                        |                         |                  |
  GitHub Read               Repo Search               Repo Patch        GitHub Write
       |                        |                         |                  |
+-----------------------------------------------------------------------------------+
|                           MultiServerMCPClient Layer                              |
+-----------------------------------------------------------------------------------+
          |                               |                                |
          v                               v                                v
+--------------------+          +--------------------+          +--------------------+
|   github_server    |          |    repo_server     |          |   sandbox_server   |
| Holds GitHub Token |          |  Holds Git Worktree|          | Holds Docker Socket|
| - get_issue        |          | - search_code      |          | - run_tests        |
| - list_comments    |          | - read_file        |          | - run_lint         |
| - create_branch    |          | - list_symbols     |          | - get_logs         |
| - push_branch      |          | - apply_patch      |          |                    |
| - open_draft_pr    |          | - git_diff         |          |                    |
+--------------------+          +--------------------+          +--------------------+
```

### Server Responsibilities
1. **`repo` Server**:
   - Manages the local isolated git worktree.
   - Operates with network access disabled and no credentials.
   - Provides agentic search (ripgrep, ast outline), file reading, unified patch application, and git diff.
2. **`sandbox` Server**:
   - The only component with access to the Docker daemon.
   - Spawns disposable containers to run pytest and ruff.
   - Enforces execution policies (resource caps, read-only mounts, timeouts).
3. **`github` Server**:
   - The only component holding the GitHub API token.
   - Scoped strictly to reading issue data and opening draft pull requests on user-owned forks.
   - Never performs auto-merge.

---

## Agent Flow & Retry Loop

```
[Issue URL]
     │
     ▼
[Issue Analyst] ──► (Extract expected behavior, calculate ambiguity)
     │
     ▼
[Code Locator]  ──► (Agentic search: ripgrep + AST symbol extraction)
     │
     ▼
[Clarification Gate] ──► Ambiguity High? ──Yes──► [Clarifier (interrupt)]
     │                                                     │
     No ◄──────────────────────────────────────────────────┘
     │
     ▼
[Fixer] ◄────────────────────────────────────────┐
     │ (Write plan, apply patch via repo MCP)   │
     ▼                                          │ (Retry: max 3 attempts)
[Test Runner] (Deterministic Docker execution)   │
     │                                          │
   Tests Pass? ──No (retries < 3) ───────────────┘
     │
    Yes (or retries exhausted)
     │
     ▼
[Reviewer] (Independent model checks diff, test tampering, regressions)
     │
   Diff Approved?
     │
    Yes
     │
     ▼
[PR Writer] (Draft description and push Draft PR via GitHub MCP)
     │
     ▼
   [End]
```

---

## Security & Isolation Rules

1. **Untrusted Data Boundary**:
   - Issue text, user comments, file contents, and tool logs are strictly treated as untrusted data, never as prompt instructions.
   - Prompts enforce strict delimiter escaping and system-prompt primacy.
2. **Network Isolation**:
   - During test execution, Docker containers have `--network none` (network disabled). Dependencies must be pre-installed during base image building.
3. **Filesystem Protections**:
   - The root filesystem of the test container is mounted read-only (`--read-only`), supplemented with constrained `tmpfs` mounts for `/tmp`.
   - Test files are mounted **READ-ONLY** inside the sandbox container to prevent the Fixer agent from tampering with test assertions to force a false pass.
4. **Credential Isolation**:
   - The Docker container receives NO GitHub token and NO LLM API keys.
   - The Docker socket is never mounted inside the sandbox container.
5. **Runtime Bounds**:
   - Non-root user execution (`nobody` or dedicated unprivileged sandbox user).
   - CPU limits (e.g. 2 cores), memory limits (e.g. 2GB), PID limits (e.g. 100), and execution timeout (e.g. 180s).
   - Hard cost cap tracked across all LLM calls per run.
