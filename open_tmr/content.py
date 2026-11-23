from dataclasses import asdict, dataclass
from typing import Iterable


@dataclass
class Concept:
    id: str
    title: str
    definition: str


@dataclass
class Topic:
    id: str
    title: str
    objectives: list[str]
    concepts: list[Concept]
    explanations: list[str]
    review_questions: list[str]


@dataclass
class Lesson:
    id: str
    title: str
    topics: list[Topic]

    def to_dict(self) -> dict:
        return asdict(self)


def validate_lesson(lesson: Lesson) -> list[str]:
    errors: list[str] = []
    if not lesson.id or not lesson.title:
        errors.append("lesson.id and lesson.title are required")
    if not lesson.topics:
        errors.append("lesson must contain at least one topic")

    for topic in lesson.topics:
        if not topic.id or not topic.title:
            errors.append("every topic requires id and title")
        if not topic.objectives:
            errors.append(f"topic {topic.id!r} requires learning objectives")
        if not topic.concepts:
            errors.append(f"topic {topic.id!r} requires concepts")
        for concept in topic.concepts:
            if not concept.id or not concept.title or not concept.definition:
                errors.append(f"topic {topic.id!r} contains an incomplete concept")
    return errors


def lesson_from_dict(value: dict) -> Lesson:
    topics = []
    for topic_value in value["topics"]:
        concepts = [Concept(**concept) for concept in topic_value["concepts"]]
        topic_value = dict(topic_value)
        topic_value["concepts"] = concepts
        topics.append(Topic(**topic_value))
    return Lesson(id=value["id"], title=value["title"], topics=topics)
