class LLMProvider:
    """Plugin interface for integration with LLM providers."""

    def configure(self, settings: dict[str, str]):
        """Configure LLM settings and instantiate objects where required."""
        raise NotImplementedError()

    def generate(self, prompt: str, files: list[bytes]) -> str:
        """Chat with the LLM provider by sending a prompt and/or file content."""
        raise NotImplementedError()
