# OpenRelik Plugins

This package introduces an architecture for dynamically loading objects at runtime. It defines a collection of lightweight interfaces and a corresponding loader/manager class. This allows our userbase to define custom logic for various actions that will consequently be called by the OpenRelik system.

The initial goal of this plugin architecture is to decouple OpenRelik from AI implementations. Given the rapid change in this sector, it allows us to focus our efforts on the overarching OpenRelik system while allowing our userbase to BYO their own LLM. It also allows us to introduce more complex conditional logic around what LLM or LLM configuration to use for a particular action ie. monomodal versus multimodal.

Example plugin implementation ie. `ollama_llm_provider.py`:
```
from openrelik_plugins.interfaces import LLMProvider
from ollama import Client

class OllamaLLMProvider(LLMProvider):

    def configure(self, settings: dict[str, str]):
        self.server_url = settings['server_url']
        self.model_name = settings['model_name']

    def generate(self, prompt: str, files: list[bytes]) -> str:
        client = Client(host=self.server_url)
        response = client.chat(
            model=self.model_name,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
```

Example plugin configuration ie. `plugins.yaml`:
```
plugins:
  llm_provider:
    default:
      module: ollama_llm_provider
      name: OllamaLLMProvider
      settings:
        server_url: http://localhost:11434
        model_name: llama3
```

Example usage:
```
>>> from openrelik_plugins import Plugins
>>> p = Plugins("plugins.yaml")
>>> p.llm_providers['default'].generate('hello', None)
"Hello! It's nice to meet you."
```
