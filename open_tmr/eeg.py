from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class EEGMetadata:
    channel_count: int
    signal_names: tuple[str, ...]
    sampling_rate_hz: float
    timestamp_source: str
    format: str
    data_classification: str = "future_interface"


def validate_eeg_metadata(value: EEGMetadata) -> list[str]:
    errors = []
    if value.channel_count != 1:
        errors.append("v0.1.0 only documents single-channel metadata; multi-channel acquisition is not implemented")
    if value.sampling_rate_hz <= 0:
        errors.append("sampling_rate_hz must be positive")
    if not value.timestamp_source:
        errors.append("timestamp_source is required")
    if value.format not in {"CSV", "WAV", "EDF", "OtherDocumentedFormat"}:
        errors.append("format must be an existing documented export format")
    if value.data_classification != "future_interface":
        errors.append("EEG metadata may not claim acquired or validated data in v0.1.0")
    return errors
