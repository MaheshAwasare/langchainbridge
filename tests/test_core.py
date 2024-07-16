import unittest
from unittest.mock import MagicMock
from llm_wrapper.core import LLMWrapper
from llm_wrapper.providers.provider_enum import LLMProvider

class TestLLMWrapper(unittest.TestCase):

    def test_google_provider_invoke(self):
        mock_google_provider = MagicMock()
        mock_google_provider.invoke.return_value = "Google response"
        wrapper = LLMWrapper(provider=LLMProvider.GOOGLE, api_key='mock_api_key')
        wrapper.llm = mock_google_provider

        response = wrapper.invoke("Test question")

        mock_google_provider.invoke.assert_called_once_with("Test question")
        self.assertEqual(response, "Google response")

    def test_openai_provider_invoke(self):
        mock_openai_provider = MagicMock()
        mock_openai_provider.invoke.return_value = "OpenAI response"
        wrapper = LLMWrapper(provider=LLMProvider.OPENAI, api_key='mock_api_key', organization='mock_org')
        wrapper.llm = mock_openai_provider

        response = wrapper.invoke("Test prompt")

        mock_openai_provider.invoke.assert_called_once_with("Test prompt")
        self.assertEqual(response, "OpenAI response")

    # Add more test cases for Ollama, Anthropic, and edge cases as needed

if __name__ == '__main__':
    unittest.main()
