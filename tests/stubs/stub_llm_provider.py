from openrelik_plugins.interfaces import LLMProvider


class StubLLMProvider(LLMProvider):

    def configure(self, settings: dict[str, str]):
        pass

    def generate(self, request: LLMProvider.GenerateRequest) -> LLMProvider.GenerateResponse:
        return LLMProvider.GenerateResponse(response=request.prompt)
