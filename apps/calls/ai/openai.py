"""Temporary OpenAI provider implementation."""

from .base import AIProvider


class OpenAIProvider(AIProvider):
    """Fake OpenAI provider used until external API integration is added."""

    def generate_response(self) -> str:
        return "Hello! I'm Nova, powered by the OpenAI provider. How can I help?"
