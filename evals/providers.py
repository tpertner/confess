"""Provider interfaces for Honesty Harness.

Today this repo ships with a tiny MockProvider so you can run the harness
without API keys. Swap in a real provider later (OpenAI / Anthropic / etc.).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Protocol


class Provider(Protocol):
    """Minimal provider interface used by the harness."""

    def generate(self, prompt: str) -> str:
        """Return a model completion for the prompt."""
        ...


@dataclass
class MockProvider:
    """A no-keys provider for local smoke tests.

    If `canned` is provided, the provider returns the first matching canned output.
    Otherwise it returns a safe default response.
    """

    canned: Optional[Dict[str, str]] = None

    def generate(self, prompt: str) -> str:
        if self.canned:
            for needle, response in self.canned.items():
                if needle in prompt:
                    return response

        # Naive default output (safe + calibrated-ish).
        return "I can’t access external updates directly. If you paste the text here, I can help summarize it."
