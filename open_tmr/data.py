from dataclasses import asdict, dataclass


@dataclass
class Session:
    schema_version: str
    session_id: str
    protocol_version: str
    software_version: str
    learning_material_id: str
    modality: str
    assessment_scores: dict
    event_timestamps: list[dict]
    data_quality_flags: list[str]
    missing_observations: list[str]
    experimental_limitations: list[str]
    participant_data_status: str = "synthetic_no_participant"

    def to_dict(self) -> dict:
        return asdict(self)


def validate_session(value: Session) -> list[str]:
    errors = []
    required = ("session_id", "protocol_version", "software_version", "learning_material_id", "modality")
    for field in required:
        if not getattr(value, field):
            errors.append(f"{field} is required")
    if value.modality not in {"auditory", "olfactory", "combined", "none"}:
        errors.append("unsupported modality")
    if value.participant_data_status != "synthetic_no_participant":
        errors.append("v0.1.0 demo sessions may only contain synthetic, non-participant data")
    return errors
