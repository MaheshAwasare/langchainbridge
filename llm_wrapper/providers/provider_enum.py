from enum import Enum

class LLMProvider(Enum):
    GOOGLE = 'google'
    OPENAI = 'openai'
    OLLAMA = 'ollama'
    ANTHROPIC = 'anthropic'
