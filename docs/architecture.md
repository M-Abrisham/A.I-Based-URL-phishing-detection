# Architecture

## Overview
TODO: high-level diagram and data flow.

## Modules
- `features.py` — URL feature extraction.
- `train.py` — model training + persistence.
- `predict.py` — model loading + inference.
- `cli.py` — command-line entry point.

## Data flow
```
raw URL → features.extract_features() → model.predict() → label
```

## Model
TODO: document chosen algorithm, hyperparameters, and evaluation metrics.
