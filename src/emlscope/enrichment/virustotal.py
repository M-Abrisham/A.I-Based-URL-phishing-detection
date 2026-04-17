"""VirusTotal enricher — looks up URLs, IPs, domains, and file hashes."""

from .base import Enricher


class VirusTotal(Enricher):
    def lookup(self, ioc: str) -> dict:
        raise NotImplementedError
