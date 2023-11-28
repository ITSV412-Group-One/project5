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
    return "http://127.0.0.1:8000"


def pytest_runtest_logstart(node_id):
    print(f"Running test: {node_id}")

def pytest_runtest_logfinish(node_id): 
    print(f"Finished test: {node_id}")
    

