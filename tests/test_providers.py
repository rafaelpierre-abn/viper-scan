from viper.providers.environment import EnvironmentProvider
import logging
import pytest

@pytest.fixture
def provider():

    return EnvironmentProvider()

def test_preprocess(provider):

    deps = """
        urllib3==1.0.0
        requests==2.0.0
        cerfifi==2024.03.02
        """ \
    .strip()

    processed = provider.preprocess(deps)
    assert isinstance(processed, list)
    assert isinstance(processed[0], dict)


def test_dependencies(provider):

    dependencies = provider.get_dependencies()
    assert dependencies