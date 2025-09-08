from openrelik_plugins.plugins import Plugins
from openrelik_plugins.interfaces import LLMProvider


def test_plugins_empty():
    c = Plugins('tests/configs/test_plugins_empty.yaml')
    assert c.get_llm_provider() == None


def test_plugins_no_plugins():
    c = Plugins('tests/configs/test_plugins_no_plugins.yaml')
    assert c.get_llm_provider() == None


def test_plugins_no_llm_provider():
    c = Plugins('tests/configs/test_plugins_no_llm_provider.yaml')
    assert c.get_llm_provider() == None


def test_plugins_stub_llm_provider():
    c = Plugins('tests/configs/test_plugins_stub_llm_provider.yaml')
    r = LLMProvider.GenerateRequest(prompt='test')
    assert c.get_llm_provider() != None


def test_plugins_stub_llm_provider_generate_default():
    c = Plugins('tests/configs/test_plugins_stub_llm_provider.yaml')
    r = LLMProvider.GenerateRequest(prompt='test')
    assert c.get_llm_provider().generate(r).response == 'default: test'


def test_plugins_stub_llm_provider_generate_notdefault():
    c = Plugins('tests/configs/test_plugins_stub_llm_provider.yaml')
    r = LLMProvider.GenerateRequest(prompt='test')
    assert c.get_llm_provider('notdefault').generate(r).response == 'notdefault: test'
