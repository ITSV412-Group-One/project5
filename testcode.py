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
@pytest.mark.parametrize("n,expected", [
  (8, [0, 1, 1, 2, 3, 5, 8]),
  (1, [0, 1]),
])
def test_fibonacci(api_url, n, expected):
  url = f"{api_url}/fibonacci/{n}"
  assert requests.get(url).json() == expected

# Factorial tests
@pytest.mark.parametrize("num,expected", [
  (4, 24),
  (5, 120),
  (0, 1),  
])
def test_factorial(api_url, num, expected):
  url = f"{api_url}/factorial/{num}"
  assert requests.get(url).json()['output'] == expected

# md5 tests
@pytest.mark.parametrize("input,expected", [
  ("test", "098f6bcd4621d373cade4e832627b4f6"),
  ("hello world", "5eb63bbbe01eeed093cb22bb8f5acdc3"),
])  
def test_md5(api_url, input, expected):
  url = f"{api_url}/md5/{input}"
  assert requests.get(url).json()['output'] == expected

if __name__ == "__main__":
  pytest.main(["-s", "testcode.py"])