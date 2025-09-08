from openrelik_plugins.interfaces import LLMProvider


class StubLLMProvider(LLMProvider):

    def configure(self, settings: dict[str, str]):
        self.prefix = settings['prefix']

    def generate(self, request: LLMProvider.GenerateRequest) -> LLMProvider.GenerateResponse:
        return LLMProvider.GenerateResponse(response=f'{self.prefix}: {request.prompt}')
