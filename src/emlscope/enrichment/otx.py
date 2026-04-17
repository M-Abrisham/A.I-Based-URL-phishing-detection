"""AlienVault OTX enricher — community threat intel pulses."""

from .base import Enricher


class OTX(Enricher):
    def lookup(self, ioc: str) -> dict:
        raise NotImplementedError
