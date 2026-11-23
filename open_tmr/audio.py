import math
import struct
import wave
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Marker:
    id: str
    frequency_hz: float
    duration_ms: int


@dataclass(frozen=True)
class AudioSegment:
    id: str
    marker: Marker
    wav_path: str


def marker_for_topic(topic_id: str) -> Marker:
    # A deterministic mapping for reproducible demonstrations, not a perceptual cue recommendation.
    values = sum(topic_id.encode("utf-8"))
    frequencies = (440.0, 660.0, 880.0)
    frequency = frequencies[values % len(frequencies)]
    return Marker(id=f"marker-{values % 1000:03d}", frequency_hz=frequency, duration_ms=180)


def generate_marker_wav(path: str | Path, marker: Marker, sample_rate: int = 48000) -> dict:
    if sample_rate < 8000:
        raise ValueError("sample_rate must be at least 8000 Hz")
    if marker.frequency_hz <= 0:
        raise ValueError("frequency_hz must be positive")

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    frames = int(sample_rate * marker.duration_ms / 1000)
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        samples = bytearray()
        fade_frames = min(int(sample_rate * 0.010), frames // 2)
        for index in range(frames):
            envelope = 1.0
            if index < fade_frames:
                envelope = index / fade_frames
            elif index >= frames - fade_frames:
                envelope = (frames - index) / fade_frames
            value = 0.12 * envelope * math.sin(2 * math.pi * marker.frequency_hz * index / sample_rate)
            samples.extend(struct.pack("<h", round(value * 32767)))
        wav.writeframes(bytes(samples))

    return {
        "format": "RIFF/WAVE PCM",
        "channels": 1,
        "sample_width_bytes": 2,
        "sample_rate_hz": sample_rate,
        "duration_ms": marker.duration_ms,
        "marker": asdict(marker),
    }
