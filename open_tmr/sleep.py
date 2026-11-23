from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass(frozen=True)
class SimulatedSleepEvent:
    timestamp: str
    event_type: str
    confidence: str
    source: str


def validate_timestamp(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def simulate_timeline(session_id: str) -> list[dict]:
    """Create clearly synthetic event labels; do not call this sleep-stage observation."""
    if not session_id:
        raise ValueError("session_id is required")
    return [
        {"timestamp": "2026-11-23T21:00:00Z", "event_type": "learning_started", "confidence": "synthetic", "source": "offline_demo"},
        {"timestamp": "2026-11-23T21:20:00Z", "event_type": "learning_completed", "confidence": "synthetic", "source": "offline_demo"},
        {"timestamp": "2026-11-23T22:00:00Z", "event_type": "simulated_nrem_window", "confidence": "synthetic", "source": "offline_demo"},
    ]


def validate_event(value: dict) -> list[str]:
    errors = []
    if not validate_timestamp(value.get("timestamp", "")):
        errors.append("valid ISO 8601 timestamp is required")
    if value.get("source") not in {"offline_demo", "sleep_as_android_export", "macrodroid_event_log", "simulated"}:
        errors.append("unsupported or undocumented event source")
    if value.get("confidence") not in {"synthetic", "phone_estimate", "unverified_export", "human_reviewed"}:
        errors.append("invalid event confidence label")
    return errors
