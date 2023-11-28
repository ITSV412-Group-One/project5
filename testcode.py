import requests
import json
import pytest
import math
from math import factorial
from dotenv import load_dotenv
import os
load_dotenv()

@pytest.fixture  
def api_url():
  if os.environ.get('DOCKER_NETWORK_MODE') == 'backend':
    return "'http://restapi:4000'"
  else:
    return "http://localhost:4000"
  
def pytest_configure(config):
    config.rootdir = '/app/testcode.py'

def test_api(api_url):
    url = f"{api_url}/test"
    res = requests.get(url)

