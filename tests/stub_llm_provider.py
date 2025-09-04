from openrelik_plugins.interfaces import LLMProvider


class StubLLMProvider(LLMProvider):

    def configure(self, settings: dict[str, str]):
        self.response = settings['response']

    def generate(self, prompt: str, files: list[bytes]) -> str:
        return self.response
