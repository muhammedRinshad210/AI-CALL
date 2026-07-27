"""Abstract contract shared by all AI response providers."""

from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Interface that every AI provider must implement."""

    @abstractmethod
    def generate_response(self) -> str:
        """Return a response for the current call conversation."""
        raise NotImplementedError
