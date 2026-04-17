# Contributing

Thanks for your interest in contributing to emlscope!

## Development setup

```bash
git clone https://github.com/M-Abrisham/emlscope.git
cd emlscope

python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

pip install -e ".[dev]"
pre-commit install

cp .env.example .env           # then fill in your API keys
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
- Good: `Add VirusTotal enricher with response caching`
- Not: `added vt stuff`

## Pull requests

- Fill out the PR template.
- Link the issue the PR closes.
- Keep PRs focused — one concern per PR.
- CI must pass before merge.

## Responsible use

emlscope is a defensive tool for SOC analysts, students, and researchers.
Don't commit real phishing payloads, live credentials, or real recipient
addresses to `tests/fixtures/` or `samples/` — scrub PII first.
