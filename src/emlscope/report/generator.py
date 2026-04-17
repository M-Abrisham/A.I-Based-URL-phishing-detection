"""Orchestrate findings into a Markdown or JSON IR report via Jinja2 templates."""


def render(findings: dict, fmt: str = "md") -> str:
    raise NotImplementedError
