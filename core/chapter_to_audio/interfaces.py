"""Type definitions and interface contracts for the reserved Chapter-to-Audio Engine."""

from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass(frozen=True)
class ChapterSummary:
    """Educational chapter-summary input."""

    chapter_id: str
    title: str
    summary_text: str
    language: str = "und"


@dataclass(frozen=True)
class Segment:
    """A planned spoken segment before audio generation or after alignment."""

    segment_id: str
    text: str
    start_seconds: float | None = None
    end_seconds: float | None = None
    research_cue_metadata: dict | None = None


@dataclass(frozen=True)
class ChapterAudioArtifact:
    """Structured result contract; audio bytes or paths are provider implementation details."""

    chapter_id: str
    segments: tuple[Segment, ...]
    audio_format: str | None = None
    audio_path: str | None = None
    metadata: dict | None = None


@runtime_checkable
class ChapterToAudioEngine(Protocol):
    """Minimal future integration interface.

    Implementations must validate inputs and outputs, preserve chapter identity,
    and return timestamps only when independently measured or formally estimated.
    """

    def convert(self, chapter: ChapterSummary) -> ChapterAudioArtifact:
        """Reserved conversion operation; no implementation is provided here."""
        ...
