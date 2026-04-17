# Contributing

Thanks for your interest in contributing!

## Development setup

```bash
git clone https://github.com/M-Abrisham/AI-Based-URL-phishing-detection.git
cd AI-Based-URL-phishing-detection

python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

pip install -e ".[dev]"
pre-commit install
```

## Workflow

1. Create a branch: `git checkout -b feat/your-feature`
2. Make your changes.
3. Run checks locally:
   ```bash
   ruff check .
   black --check .
   pytest
   ```
4. Commit (pre-commit hooks will run automatically).
5. Push and open a pull request against `main`.

## Branch naming

- `feat/<short-name>` — new features
- `fix/<short-name>` — bug fixes
- `docs/<short-name>` — documentation
- `chore/<short-name>` — tooling, config, refactor

## Commit messages

Short, imperative mood:
- Good: `Add TF-IDF character n-gram features`
- Not: `added some features`

## Pull requests

- Fill out the PR template.
- Link the issue the PR closes.
- Keep PRs focused — one concern per PR.
- CI must pass before merge.
