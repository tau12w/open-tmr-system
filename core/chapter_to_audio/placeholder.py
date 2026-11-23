"""Explicit unsupported placeholder for the future Chapter-to-Audio Engine."""

from .interfaces import ChapterAudioArtifact, ChapterSummary, ChapterToAudioEngine


class NotImplementedChapterToAudioEngine:
    """Placeholder satisfying no runtime behavior and making unsupported use explicit."""

    def convert(self, chapter: ChapterSummary) -> ChapterAudioArtifact:
        raise NotImplementedError(
            "The Chapter-to-Audio Engine is reserved; conversion is not implemented."
        )


def require_future_engine() -> ChapterToAudioEngine:
    """Return a placeholder engine. This function does not perform conversion."""

    return NotImplementedChapterToAudioEngine()
