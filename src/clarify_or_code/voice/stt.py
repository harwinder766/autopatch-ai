"""Speech-to-text (STT) interface for developer clarification.

Purpose: Captures spoken developer responses (e.g. in Hinglish via Gnani Prisma) and snaps names to repo symbols using rapidfuzz.
Phase: Phase 9 (Post-MVP Voice Layer stub).
Serves: Clarifier agent spoken interaction.
"""

from typing import Any


class VoiceSTTClient:
    """Streams and transcribes spoken audio responses."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key

    def transcribe_audio_stream(self, audio_stream: Any) -> str:
        """Transcribe streaming audio into raw text."""
        raise NotImplementedError("Streaming STT transcription stub. Implemented in Phase 9.")

    def snap_to_symbols(self, transcribed_text: str, valid_symbols: list[str]) -> str:
        """Correct phonetically transcribed identifiers to match real codebase symbols using fuzzy matching."""
        raise NotImplementedError("Fuzzy symbol snapping stub. Implemented in Phase 9.")
