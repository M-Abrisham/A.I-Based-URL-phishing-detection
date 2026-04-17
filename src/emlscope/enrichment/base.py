"""Abstract base class for threat-intel enrichers."""

from abc import ABC, abstractmethod


class Enricher(ABC):
    @abstractmethod
    def lookup(self, ioc: str) -> dict: ...
