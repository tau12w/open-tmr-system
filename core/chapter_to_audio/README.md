# Chapter-to-Audio Engine

## Status

**Reserved module; not implemented.** This directory exists to define future integration boundaries only. It does not perform text-to-speech, audio rendering, timing extraction, or research-cue generation.

## Intended purpose

The Chapter-to-Audio Engine is a planned standalone software component that would convert educational chapter summaries into:

- normalized text segments;
- generated spoken audio;
- segment start/end timestamps;
- research cue metadata;
- export metadata for downstream systems.

No use of the engine is currently assumed in the existing `open_tmr` demo.

## Planned architecture

A future implementation may contain:

- an input parser for a defined summary format;
- a segment planner for headings, objectives, concepts, and explanations;
- a speech synthesis adapter boundary;
- timestamp alignment and validation;
- neutral research-cue metadata annotation;
- an exporter for JSON and audio manifests.

Provider-specific or platform-specific code should remain behind adapters and should not be placed in the shared interface.

## Clean interface

See `interfaces.py`. Future implementations must preserve the request/result types and raise explicit unsupported errors until behavior is validated.

## Independence requirements

This module must remain independent from:

- EEG acquisition or signal processing;
- sleep monitoring or sleep-stage estimation;
- auditory stimulation delivery;
- olfactory hardware or delivery;
- participant scheduling or overnight automation.

The module may accept generic educational text and emit metadata. It must not import or call those components.

## Incomplete placeholders

- `interfaces.py`: data types and abstract interface; no implementation.
- `placeholder.py`: explicit unsupported-operation placeholder; no speech or audio generation.
- `__init__.py`: module exports only.

## Required before implementation

1. Approved input and output schemas.
2. Deterministic test fixtures.
3. Timestamp measurement method.
4. Speech adapter test strategy.
5. Copyright and licensing review for input and voices.
6. Safety, accessibility, and privacy review.
7. Integration tests independent of research delivery modules.
