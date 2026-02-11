from dataclasses import dataclass
from typing import Protocol

class Provider(Protocol):
    def generate(self, prompt: str) -> str:
        ...

@dataclass
class MockProvider:
    """Replace with OpenAI/Anthropic/etc. later.
    This is intentionally boring so the harness runs without keys.
    """
    canned: dict[str, str] | None = None

    def generate(self, prompt: str) -> str:
        if self.canned:
            for k, v in self.canned.items():
                if k in prompt:
                    return v
        # naive default output (safe + calibrated-ish)
        return "I can’t access external updates directly. If you paste the text here, I can help summarize it."
