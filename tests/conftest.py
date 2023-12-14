# conftest.py
import pytest
from dotenv import load_dotenv

@pytest.fixture(autouse=True, scope='session')
def set_env_vars():
    load_dotenv(".env", verbose=True)
