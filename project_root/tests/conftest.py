# conftest.py
import os
import pytest

@pytest.fixture(autouse=True, scope='session')
def set_env_vars():
    os.environ['RIOT_API_KEY'] = 'mock_api_key'
