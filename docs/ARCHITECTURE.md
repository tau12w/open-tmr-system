# Architecture

## Repository boundaries

- `open_tmr/` contains the existing Python package and offline demonstration.
- `docs/` contains project-level documentation.
- `research/` contains methodology and research-maintenance documents.
- `core/chapter_to_audio/` is a reserved, independent future software component.
- Existing EEG, sleep, and cue code remains in `open_tmr/` and has explicit disabled or placeholder boundaries.

## Data flow in the current demo

```text
Lesson model -> validation -> educational topic metadata
             -> deterministic marker metadata -> synthetic PCM WAV
Lesson/cue models -> JSON metadata -> validation report
```

The demo is synthetic and offline. It does not perform text-to-speech or human-subject data acquisition.

## Chapter-to-Audio Engine planned boundary

The future engine should accept chapter-summary input and emit structured plans and audio artifacts through explicitly typed interfaces. It should not import or depend on EEG, sleep, or olfactory modules.

A planned pipeline, not current behavior:

```text
Summary document
  -> normalized chapter model
  -> segment planner
  -> speech adapter (future)
  -> timestamp calculator (future)
  -> research cue annotator (future)
  -> structured artifact
```

Each stage requires independent validation and testing before integration.

## Interface contract

The placeholder defines an abstract `ChapterToAudioEngine` interface and typed request/result models. A future implementation may add local or provider-specific speech adapters, but it must keep provider credentials and network behavior outside the core interface.

## Dependency isolation

The reserved module must not import:

- `open_tmr.eeg`;
- `open_tmr.sleep`;
- olfactory delivery code;
- overnight scheduling or participant-stimulation code.

It may consume generic educational text and emit neutral metadata. Research-cue metadata is descriptive and must not imply approved cue delivery.
