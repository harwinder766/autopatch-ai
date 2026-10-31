"""Cost tracking and budget management.

Purpose: Tracks token consumption, computes USD costs across model tiers, and halts runs exceeding the hard cap.
Phase: Phase 0 (Foundation stub), implemented in Phase 1.
Serves: LLM client and Supervisor agent.
"""

from pydantic import BaseModel, Field


class CostTracker(BaseModel):
    """Tracks token usage and accumulated cost in USD."""

    hard_cap_usd: float = Field(default=2.50, description="Maximum allowed spend per run in USD")
    total_spent_usd: float = Field(default=0.0, description="Total amount spent across all agent calls")
    total_prompt_tokens: int = Field(default=0, description="Total prompt tokens consumed")
    total_completion_tokens: int = Field(default=0, description="Total completion tokens consumed")

    def record_usage(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        """Compute cost for call, record tokens, and verify against hard cap."""
        raise NotImplementedError("Cost tracking stub. Implemented in Phase 1.")

    def is_exceeded(self) -> bool:
        """Check if current spend has reached or exceeded hard budget cap."""
        return self.total_spent_usd >= self.hard_cap_usd
