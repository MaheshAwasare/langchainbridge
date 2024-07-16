import unittest
from unittest.mock import patch
from llm_wrapper.providers.google_provider import GoogleProvider
from llm_wrapper.providers.openai_provider import OpenAIProvider
from llm_wrapper.providers.ollama_provider import OllamaProvider
from llm_wrapper.providers.anthropic_provider import AnthropicProvider

class TestGoogleProvider(unittest.TestCase):

    def test_google_provider_invoke(self):
        provider = GoogleProvider(api_key='mock_api_key', model='mock_model', temperature=0.8)
        with patch.object(provider.llm, 'invoke', return_value="Google response") as mock_method:
            response = provider.invoke("Test question")
            mock_method.assert_called_once_with({"question": "Test question"})
            self.assertEqual(response, "Google response")

class TestOpenAIProvider(unittest.TestCase):

    def test_openai_provider_invoke(self):
        provider = OpenAIProvider(api_key='mock_api_key', organization='mock_org')
        with patch.object(provider.llm, 'invoke', return_value="OpenAI response") as mock_method:
            response = provider.invoke("Test prompt")
            mock_method.assert_called_once_with("Test prompt")
            self.assertEqual(response, "OpenAI response")

class TestOllamaProvider(unittest.TestCase):

    def test_ollama_provider_invoke(self):
        provider = OllamaProvider(model='mock_model', endpoint='mock_endpoint', system_prompt='mock_prompt')
        with patch('requests.post') as mock_post:
            mock_post.return_value.json.return_value = {"ollama_response": "Mock Ollama response"}
            response = provider.invoke("Test input")
            mock_post.assert_called_once()
            self.assertIn('prompt', mock_post.call_args[1]['json'])
            self.assertEqual(response, {"ollama_response": "Mock Ollama response"})

class TestAnthropicProvider(unittest.TestCase):

    def test_anthropic_provider_invoke(self):
        provider = AnthropicProvider(api_key='mock_api_key', model='mock_model', temperature=0.5, max_tokens=100)
        with patch.object(provider.llm, 'invoke', return_value="Anthropic response") as mock_method:
            response = provider.invoke("Test message")
            mock_method.assert_called_once()
            self.assertEqual(response, "Anthropic response")

if __name__ == '__main__':
    unittest.main()
