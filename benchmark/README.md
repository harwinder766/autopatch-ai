# Benchmark Dataset: Clarify-or-Code

## Overview
This directory contains the benchmark task suite used to empirically evaluate Clarify-or-Code.

The benchmark consists of 40 to 60 bug-fixing tasks mined from 5 to 8 small-to-medium Python repositories with working pytest suites using PyDriller (Phase 6).

## Task Schema
Each line in `tasks.jsonl` is a JSON object with:
- `task_id`: Unique identifier (e.g. `pallets-click-1234`).
- `repo_url`: Target repository clone URL.
- `base_commit`: Commit hash immediately prior to the fix.
- `issue_url`: Link to the resolved GitHub issue.
- `issue_text`: Issue title, description, and discussion comments.
- `test_patch`: Associated pytest regression test patch (concealed during agent runs).
- `ground_truth_patch`: Human developer solution patch (concealed during agent runs).

## Experimental Arms
Benchmark runs compare:
1. **Never Ask**: Gating disabled, agent always proceeds directly to patch formulation.
2. **Always Ask**: Clarifier agent interrupts on 100% of tasks.
3. **Rule-Based Gate**: Interruption triggered when ambiguity > threshold or stack trace is absent.
4. **Learned Gate**: LightGBM model predicting failure risk based on contextual features.
5. **Ablations**: Single-agent baseline vs. multi-agent graph; retry loop on vs. off; with vs. without Reviewer agent.
