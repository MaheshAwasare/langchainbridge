from langchain_google_genai import ChatGoogleGenerativeAI
from .base_provider import BaseProvider

class GoogleProvider(BaseProvider):
    def __init__(self, api_key, **kwargs):
        super().__init__(api_key)
        self.model = kwargs.get('model', 'gemini-pro')
        self.temperature = kwargs.get('temperature', 0.9)
        self.llm = ChatGoogleGenerativeAI(model=self.model, temperature=self.temperature, google_api_key=self.api_key)

    def invoke(self, input_data):
        return self.llm.invoke({"question": input_data})
