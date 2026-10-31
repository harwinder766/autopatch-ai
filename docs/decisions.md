# Architectural Decisions

This document records the foundational architectural decisions for Clarify-or-Code, each accompanied by its rationale. These decisions supersede any conflicting details in early planning documents.

1. **Agentic Search over Vector Embeddings in MVP**: Agentic keyword grep (ripgrep) combined with AST symbol outlining is faster, deterministic, requires zero embedding index management, and matches human developer navigation patterns for small-to-medium repos.
2. **Git Worktrees Cached by Repo + Commit SHA**: Worktrees provide lightweight, zero-interference branch isolation per task while amortizing repository clone bandwidth through local object caching without persistent index state.
3. **Hardened Docker Sandbox with Read-Only Test Mounts**: Running unprivileged with network disabled, resource bounds, and read-only test mounts guarantees code isolation and prevents the LLM from tampering with tests to fabricate passes.
4. **Strict Untrusted Data Boundary with Full Tool Call Logging**: External text (issues, comments, file contents, logs) must never be interpreted as agent instructions to prevent prompt injection and ensure complete auditability of all agent actions.
5. **LiteLLM Provider Abstraction with Configurable Model Tiers and Cost Caps**: LiteLLM enables dynamic routing across model tiers (strong patching model, cheap analysis model, independent reviewer) while strictly enforcing hard budget caps per task.
6. **Voice Clarification Deferred as Phase 9 Stubs**: Voice input/output (Prisma STT / Timbre TTS) is an auxiliary interaction layer that adds complexity without altering the core research question of clarification gating.
