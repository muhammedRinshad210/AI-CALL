"""Provider-independent application services for AI call responses."""

from django.conf import settings

from .ai.base import AIProvider
from .ai.gemini import GeminiProvider
from .ai.openai import OpenAIProvider


PROVIDERS: dict[str, type[AIProvider]] = {
    "gemini": GeminiProvider,
    "openai": OpenAIProvider,
}


def get_ai_provider() -> AIProvider:
    """Build the configured provider, safely defaulting to Gemini."""
    provider_name = getattr(settings, "AI_PROVIDER", "gemini").strip().lower()
    provider_class = PROVIDERS.get(provider_name, GeminiProvider)
    return provider_class()


def get_ai_response() -> str:
    """Return an AI response without coupling callers to a provider."""
    return get_ai_provider().generate_response()
