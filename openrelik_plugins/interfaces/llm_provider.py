class LLMProvider:
    """Plugin interface for integration with LLM providers."""

    def configure(self, settings: dict[str, str]):
        """Configure LLM settings and instantiate objects where required."""
        raise NotImplementedError()

    class GenerateRequest:
        def __init__(self, prompt: str = None, files: list[bytes] = None):
            self.prompt = prompt
            self.files = files

    class GenerateResponse:
        def __init__(self, response: str = None):
            self.response = response

    def generate(self, request: GenerateRequest) -> GenerateResponse:
        """Chat with the LLM provider by sending a prompt and/or file content."""
        raise NotImplementedError()
