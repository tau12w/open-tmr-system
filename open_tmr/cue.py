from dataclasses import asdict, dataclass
from enum import Enum


class Modality(str, Enum):
    AUDITORY = "auditory"
    OLFACTORY = "olfactory"


@dataclass(frozen=True)
class CueAssociation:
    schema_version: str
    learning_session_id: str
    topic_id: str
    audio_segment_id: str
    cue_id: str
    modality: str
    association_metadata: dict

    def to_dict(self) -> dict:
        return asdict(self)


def create_association(
    learning_session_id: str,
    topic_id: str,
    audio_segment_id: str,
    cue_id: str,
    modality: Modality,
) -> CueAssociation:
    modality_metadata = (
        {"delivery_state": "not_implemented", "stimulation_state": "disabled"}
        if modality == Modality.OLFACTORY
        else {"sine_marker": True, "delivery_state": "synthetic_only", "stimulation_state": "disabled"}
    )
    return CueAssociation(
        schema_version="1.0",
        learning_session_id=learning_session_id,
        topic_id=topic_id,
        audio_segment_id=audio_segment_id,
        cue_id=cue_id,
        modality=modality.value,
        association_metadata=modality_metadata,
    )


def validate_association(value: CueAssociation) -> list[str]:
    errors = []
    if value.modality not in {item.value for item in Modality}:
        errors.append("unsupported cue modality")
    for field in ("learning_session_id", "topic_id", "audio_segment_id", "cue_id"):
        if not getattr(value, field):
            errors.append(f"{field} is required")
    return errors
