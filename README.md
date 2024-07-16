# LangChainBridge

LangChainBridge is a unified wrapper library designed to simplify the use of various Large Language Model (LLM) providers such as Google, OpenAI, Ollama, and Anthropic. By using LangChainBridge, developers can interact with multiple LLMs through a single, consistent interface, reducing complexity and minimizing the risk of errors.

## Features

- **Unified API**: Interact with different LLM providers through a common interface.
- **Easy Integration**: Quickly switch between LLM providers without changing your code logic.
- **Extensibility**: Easily add support for new LLM providers as needed.

## Installation

Install LangChainBridge using pip:

```sh
pip install langchainbridge

```
## Supported Providers
- Google Generative AI
- OpenAI
- Ollama
- Anthropic

## Usage
### Initialize the Wrapper
You can initialize the wrapper by specifying the provider using the LLMProvider enum and providing the necessary API key and other parameters.

```shell
from langchainbridge.core import LLMWrapper
from langchainbridge.providers.provider_enum import LLMProvider

# For Google
google_llm = LLMWrapper(provider=LLMProvider.GOOGLE, api_key='YOUR_GOOGLE_API_KEY')
response = google_llm.invoke("Where was Shivaji Maharaj born?")
print(response)

# For OpenAI
openai_llm = LLMWrapper(provider=LLMProvider.OPENAI, api_key='YOUR_OPENAI_API_KEY', organization='YOUR_ORG_ID')
response = openai_llm.invoke("What NFL team won the Super Bowl in the year Justin Bieber was born?")
print(response)

# For Ollama
ollama_llm = LLMWrapper(provider=LLMProvider.OLLAMA)
response = ollama_llm.invoke("Summarize the text given to you.")
print(response)

# For Anthropic
anthropic_llm = LLMWrapper(provider=LLMProvider.ANTHROPIC, api_key='YOUR_ANTHROPIC_API_KEY')
response = anthropic_llm.invoke("Translate 'I love programming.' to French.")
print(response)

```

