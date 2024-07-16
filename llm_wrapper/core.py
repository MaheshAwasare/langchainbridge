from .providers.google_provider import GoogleProvider
from .providers.openai_provider import OpenAIProvider
from .providers.ollama_provider import OllamaProvider
from .providers.anthropic_provider import AnthropicProvider
from .providers.provider_enum import LLMProvider

class LLMWrapper:
    def __init__(self, provider: LLMProvider, api_key=None, **kwargs):
        self.provider = provider
        self.api_key = api_key
        self.kwargs = kwargs
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        if self.provider == LLMProvider.GOOGLE:
            return GoogleProvider(api_key=self.api_key, **self.kwargs)
        elif self.provider == LLMProvider.OPENAI:
            return OpenAIProvider(api_key=self.api_key, **self.kwargs)
        elif self.provider == LLMProvider.OLLAMA:
            return OllamaProvider(**self.kwargs)
        elif self.provider == LLMProvider.ANTHROPIC:
            return AnthropicProvider(api_key=self.api_key, **self.kwargs)
        else:
            raise ValueError("Unsupported provider")

    def invoke(self, input_data):
        return self.llm.invoke(input_data)
