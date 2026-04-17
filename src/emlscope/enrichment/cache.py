"""Local JSON cache so we don't burn API quotas on repeat lookups."""


def get(key: str) -> dict | None:
    raise NotImplementedError


def put(key: str, value: dict) -> None:
    raise NotImplementedError
