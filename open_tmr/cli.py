import json
from pathlib import Path

from open_tmr.audio import generate_marker_wav, marker_for_topic
from open_tmr.content import Concept, Lesson, Topic, validate_lesson
from open_tmr.cue import Modality, create_association, validate_association
from open_tmr.data import Session, validate_session
from open_tmr.sleep import simulate_timeline, validate_event


def build_lesson() -> Lesson:
    return Lesson(
        id="lesson-sleep-consolidation-001",
        title="Memory Consolidation Basics",
        topics=[
            Topic(
                id="topic-memory-stages",
                title="Encoding and consolidation",
                objectives=["Distinguish encoding from consolidation."],
                concepts=[Concept(id="concept-encoding", title="Encoding", definition="The initial processing of information into a retrievable memory representation.")],
                explanations=["Memory processes continue after initial learning. Sleep is associated with the reorganization of memory representations."],
                review_questions=["How does consolidation differ from encoding?"],
            )
        ],
    )


def demo(output_dir: str = "demo_output") -> dict:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    lesson = build_lesson()
    lesson_errors = validate_lesson(lesson)
    if lesson_errors:
        raise RuntimeError("lesson validation failed: " + "; ".join(lesson_errors))

    wav_metadata = []
    associations = []
    for topic in lesson.topics:
        segment_id = f"segment-{topic.id}"
        marker = marker_for_topic(topic.id)
        wav_path = output / f"{segment_id}.wav"
        wav_metadata.append({**generate_marker_wav(wav_path, marker), "path": wav_path.as_posix(), "segment_id": segment_id})
        association = create_association("session-demo-synthetic-001", topic.id, segment_id, marker.id, Modality.AUDITORY)
        association_errors = validate_association(association)
        if association_errors:
            raise RuntimeError("association validation failed: " + "; ".join(association_errors))
        associations.append(association.to_dict())

    session = Session(
        schema_version="1.0",
        session_id="session-demo-synthetic-001",
        protocol_version="demo-0.1.0",
        software_version="0.1.0",
        learning_material_id=lesson.id,
        modality="auditory",
        assessment_scores={},
        event_timestamps=simulate_timeline("session-demo-synthetic-001"),
        data_quality_flags=["synthetic_data", "no_hardware_acquisition"],
        missing_observations=["all real participant observations"],
        experimental_limitations=["offline demonstration only", "not a TMR experiment", "no sleep-stage validation"],
    )
    session_errors = validate_session(session)
    if session_errors:
        raise RuntimeError("session validation failed: " + "; ".join(session_errors))

    for event in session.event_timestamps:
        event_errors = validate_event(event)
        if event_errors:
            raise RuntimeError("event validation failed: " + "; ".join(event_errors))

    (output / "lesson.json").write_text(json.dumps(lesson.to_dict(), indent=2) + "\n", encoding="utf-8")
    (output / "audio_metadata.json").write_text(json.dumps({"synthetic": True, "segments": wav_metadata}, indent=2) + "\n", encoding="utf-8")
    (output / "cue_associations.json").write_text(json.dumps({"synthetic": True, "associations": associations}, indent=2) + "\n", encoding="utf-8")
    (output / "session.json").write_text(json.dumps(session.to_dict(), indent=2) + "\n", encoding="utf-8")
    (output / "validation.txt").write_text(
        "VALID: synthetic lesson\nVALID: synthetic WAV metadata\nVALID: synthetic auditory cue association\nVALID: simulated event timeline\nVALID: synthetic session\n",
        encoding="utf-8",
    )

    return {"output": str(output), "lesson": lesson.id, "session": session.session_id, "segments": len(wav_metadata)}
