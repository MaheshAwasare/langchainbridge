import requests
from .base_provider import BaseProvider

class OllamaProvider(BaseProvider):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = kwargs.get('model', 'phi')
        self.endpoint = kwargs.get('endpoint', 'http://localhost:11434/api/generate')
        self.system_prompt = kwargs.get('system_prompt', 'Your goal is to summarize the text given to you.')

    def invoke(self, input_data):
        ollama_prompt = f"{self.system_prompt}: {input_data}"
        ollama_data = {
            "model": self.model,
            "prompt": ollama_prompt,
            "stream": False,
            "keep_alive": "1m",
        }
        response = requests.post(self.endpoint, json=ollama_data)
        return response.json()
