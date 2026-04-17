"""AbuseIPDB enricher — reputation for IPv4/IPv6 addresses."""

from .base import Enricher


class AbuseIPDB(Enricher):
    def lookup(self, ioc: str) -> dict:
        raise NotImplementedError
