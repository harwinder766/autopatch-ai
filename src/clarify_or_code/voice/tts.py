"""Text-to-speech (TTS) interface for clarifying questions.

Purpose: Converts Clarifier question text into synthesized audio prompts via Timbre TTS.
Phase: Phase 9 (Post-MVP Voice Layer stub).
Serves: Clarifier agent spoken interaction.
"""


class VoiceTTSClient:
    """Synthesizes question text to audio."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key

    def synthesize_speech(self, text: str) -> bytes:
        """Convert text into synthesized audio bytes."""
        raise NotImplementedError("TTS synthesis stub. Implemented in Phase 9.")
