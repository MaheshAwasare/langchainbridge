from langchain_anthropic import ChatAnthropic
from .base_provider import BaseProvider

class AnthropicProvider(BaseProvider):
    def __init__(self, api_key, **kwargs):
        super().__init__(api_key)
        self.model = kwargs.get('model', 'claude-3-5-sonnet-20240620')
        self.temperature = kwargs.get('temperature', 0)
        self.max_tokens = kwargs.get('max_tokens', 1024)
        self.llm = ChatAnthropic(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            api_key=self.api_key
        )

    def invoke(self, input_data):
        messages = [
            ("system", "You are a helpful assistant that translates English to French. Translate the user sentence."),
            ("human", input_data)
        ]
        return self.llm.invoke(messages)
