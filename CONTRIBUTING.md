# Contributing

## Setup

```bash
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
```

## Development rules

- Keep the offline demo free of API keys and paid services.
- Label simulated, synthetic, and proposed features clearly.
- Do not add unreviewed overnight sensory stimulation.
- Do not add hardware protocols without actual manufacturer documentation.
- Do not represent estimated sleep stages as EEG-confirmed stages.
- Never commit identifiable participant data or secrets.
- Add tests for new data validation and core behavior.
- Prefer the Python standard library unless a dependency is justified.

## Pull requests

Use a focused change: explain the scientific or engineering need, list tested behavior, identify assumptions, and report unresolved information.
