# Project Vision

## Purpose

Open TMR System is an experimental, offline-first research software prototype for structured educational content and Targeted Memory Reactivation (TMR) metadata.

The project supports reproducible software demonstrations and clearly bounded research planning. It does not provide a medical device, clinical sleep assessment, or validated intervention.

## Chapter-to-Audio Engine role

The reserved `core/chapter_to_audio/` module will, if implemented and validated, convert educational chapter summaries into:

- a structured spoken-audio plan;
- segment-level text and timing metadata;
- optional research cues and cue provenance;
- machine-readable artifacts for review and integration.

For the current release, the engine does not convert text, generate speech, synthesize audio, or add cues. It is a non-operational interface reserve.

## Goals

1. Keep educational content separate from stimulation behavior.
2. Prefer explicit schemas and validated metadata over hidden assumptions.
3. Make synthetic demonstrations reproducible and clearly labeled.
4. Preserve an offline-first design with no required API keys or network access.
5. Prevent auditory, EEG, sleep-monitoring, and olfactory work from being silently coupled.
6. Require evidence and qualified oversight before human-subject research.

## Non-goals

- Clinical sleep-stage classification.
- EEG or wearable control.
- Overnight stimulus delivery to sleeping participants.
- Olfactory delivery or hardware control.
- Medical diagnosis or treatment.
- Presentation of synthetic output as participant evidence.

## Current status

The existing Python package provides synthetic lesson structures, deterministic acoustic markers, cue metadata, simulated sessions, and offline demo artifacts. The Chapter-to-Audio Engine is not implemented.
