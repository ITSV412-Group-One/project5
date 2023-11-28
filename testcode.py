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
    return "http://api:4000"
  else:
    return "http://127.0.0.1:8000"


def pytest_runtest_logstart(node_id):
    print(f"Running test: {node_id}")

def pytest_runtest_logfinish(node_id): 
    print(f"Finished test: {node_id}")
    

# Fibonacci tests  
@pytest.mark.parametrize("endpoint,status_code", [
    ("/fibonacci/6", 200),
    ("/fibonacci/invalid", 400)
]) 
def test_fibonacci_response_codes(api_url, endpoint, status_code):

   url = f"{api_url}{endpoint}"
   res = requests.get(url)
@pytest.mark.parametrize("n,expected", [
  (8, [0, 1, 1, 2, 3, 5, 8]),
  (1, [0, 1]),
])
def test_fibonacci(api_url, n, expected):
  url = f"{api_url}/fibonacci/{n}"
  assert requests.get(url).json() == expected


if __name__ == "__main__":
  pytest.main(["-s", "testcode.py"])