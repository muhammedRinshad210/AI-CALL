"""Google Gemini provider for AI call responses."""

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from .base import AIProvider


class GeminiProvider(AIProvider):
    """Generate plain-text replies with Google's Gemini API."""

    model = "gemini-2.5-flash"

    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()

    def reply(self, user_message: str) -> str:
        """Return a friendly plain-text Gemini reply or a safe fallback."""
        if not self.api_key:
            return "I'm ready to help, but my AI connection is not configured yet."

        if not user_message or not user_message.strip():
            return "Please tell me a little more about what you need help with."

        try:
            client = genai.Client(
                api_key=self.api_key,
                http_options=types.HttpOptions(timeout=10000),
            )
            response = client.models.generate_content(
                model=self.model,
                contents=user_message.strip(),
            )
            message = (response.text or "").strip()

            if not message:
                return "I didn't receive a complete response. Could you try again?"

            return message
        except TimeoutError:
            return "The AI connection took too long. Please try again in a moment."
        except Exception:
            return "I couldn't reach the AI service right now. Please try again shortly."

    def generate_response(self) -> str:
        """Preserve the existing provider interface used by the service layer."""
        return self.reply("Hello! Please introduce yourself and offer help.")
