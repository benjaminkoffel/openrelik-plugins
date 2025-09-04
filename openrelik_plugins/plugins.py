from importlib import import_module
from yaml import safe_load
from .interfaces import LLMProvider
from typing import Any


def load_llm_provider(module: str, name: str, settings: dict[str, str]) -> type[LLMProvider]:
    """Instantiate and configure an LLMProvider object."""
    m = import_module(module)
    c = getattr(m, name)
    if not issubclass(c, LLMProvider):
        print(f'ERROR: Plugin {module}/{name} does not implement LLMProvider.')
        exit(1)
    i = c()
    i.configure(settings)
    return i


class Plugins:
    """Load plugins and maintain a pointer to instantiated objects."""

    def __init__(self, path: str):
        with open(path, 'r') as r:
            c = safe_load(r) or {}
        p = c.get('plugins') or {}
        l = p.get('llm_provider') or {}
        self.llm_providers: dict[str, type[LLMProvider]] = {
            k: load_llm_provider(v['module'], v['name'], v['settings'])
            for k, v in l.items()
        }
