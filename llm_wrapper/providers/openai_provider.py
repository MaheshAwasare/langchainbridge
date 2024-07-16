from langchain_openai import OpenAI
from .base_provider import BaseProvider

class OpenAIProvider(BaseProvider):
    def __init__(self, api_key, **kwargs):
        super().__init__(api_key)
        self.organization = kwargs.get('organization')
        self.llm = OpenAI(openai_api_key=self.api_key, openai_organization=self.organization)

    def invoke(self, input_data):
        return self.llm.invoke(input_data)
