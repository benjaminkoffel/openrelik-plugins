# import pytest
from openrelik_plugins.plugins import Plugins
from stub_llm_provider import StubLLMProvider


def test_plugins_empty():
    c = Plugins('tests/test_plugins_empty.yaml')
    assert c.llm_providers == {}


def test_plugins_no_plugins():
    c = Plugins('tests/test_plugins_no_plugins.yaml')
    assert c.llm_providers == {}


def test_plugins_no_llm_provider():
    c = Plugins('tests/test_plugins_no_llm_provider.yaml')
    assert c.llm_providers == {}


def test_plugins_stub_llm_provider():
    c = Plugins('tests/test_plugins_stub_llm_provider.yaml')
    assert 'default' in c.llm_providers
    assert isinstance(c.llm_providers['default'], StubLLMProvider)
    assert c.llm_providers['default'].response == 'test'
    assert c.llm_providers['default'].generate(None, None) == 'test'
