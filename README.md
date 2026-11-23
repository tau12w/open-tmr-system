# Open TMR System

Open TMR System is an experimental, offline-first research software prototype for structured educational audio and Targeted Memory Reactivation (TMR) metadata.

**This v0.1.0 release is a software demonstration, not a real TMR experiment.** It does not acquire EEG, control sleep, deliver sensory stimuli to sleeping people, or infer clinical sleep stages.

**Repository:** https://github.com/tau12w/open-tmr-system

## Research title

“Comparative Evaluation of Auditory and Olfactory Targeted Memory Reactivation for Educational Memory Retention.”

## Two-minute offline demo

Python 3.10 or newer is the only requirement.

```bash
python -m open_tmr.cli demo
python -m unittest discover -s tests -v
```

The demo creates `demo_output/` containing generated WAV files, a lesson JSON file, cue associations, sample session JSON, a simulated event timeline, and validation output. Everything is synthetic and locally generated.

## Installation

```bash
python -m pip install -e .
open-tmr demo
```

No API keys, internet access, EEG hardware, smartphones, or paid services are required.

## Repository layout

```text
open_tmr/          Core Python package
examples/          Synthetic lesson, session, and event data
schemas/           Versioned JSON schemas
protocols/         Research and safety documentation
docs/              Literature and software documentation
integrations/      Placeholder descriptions for future exports and drivers
core/              Reserved standalone modules, including Chapter-to-Audio
tests/             Automated tests
.github/workflows/ Continuous integration
```

## Scientific safeguards

- Demonstrations are awake-only or simulated.
- Phone-based sleep estimates are not presented as EEG-confirmed sleep stages.
- Auditory and olfactory modalities have separate metadata and associations.
- Overnight cue delivery and sleeping-participant stimulation are not implemented.
- The EEG module is a future interface only; no Bioamp protocol or specifications are assumed.
- Synthetic data are never represented as participant observations.
- Participants, if studied in future authorized work, require informed consent/assent and applicable ethics review, qualified oversight, privacy controls, and data governance.

## Core modules

- `open_tmr/content.py`: editable educational content and validation.
- `open_tmr/audio.py`: deterministic, dependency-free WAV generation and metadata.
- `open_tmr/cue.py`: versioned auditory and olfactory cue associations.
- `open_tmr/sleep.py`: documented export import boundaries and simulated timelines.
- `open_tmr/eeg.py`: sampling, signal-quality, and missing-data metadata abstractions.
- `open_tmr/data.py`: anonymized synthetic session models and validation.
- `open_tmr/cli.py`: offline demo and validation commands.
- `core/chapter_to_audio/`: reserved Chapter-to-Audio interface and unsupported placeholder.

## Limitations

This release cannot estimate sleep stages, classify EEG, verify hardware safety, implement TTS providers, or serve as an experimental protocol. It contains no TTS API integration and no copyrighted source text.
