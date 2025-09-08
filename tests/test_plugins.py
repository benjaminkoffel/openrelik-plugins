from openrelik_plugins.plugins import Plugins
from openrelik_plugins.interfaces import LLMProvider


def test_plugins_empty():
    c = Plugins('tests/configs/test_plugins_empty.yaml')
    assert c.llm_providers == {}


def test_plugins_no_plugins():
    c = Plugins('tests/configs/test_plugins_no_plugins.yaml')
    assert c.llm_providers == {}


def test_plugins_no_llm_provider():
    c = Plugins('tests/configs/test_plugins_no_llm_provider.yaml')
    assert c.llm_providers == {}


def test_plugins_stub_llm_provider():
    c = Plugins('tests/configs/test_plugins_stub_llm_provider.yaml')
    r = LLMProvider.GenerateRequest(prompt='test')
    assert c.llm_providers['default'].generate(r).response == 'test'
