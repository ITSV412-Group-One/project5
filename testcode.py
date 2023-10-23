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
  return "http://localhost:8000"

# Mel
# a function to test the /md5/<string> endpoint 
@pytest.mark.parametrize("test_string", [
  "hello",
  "test" 
])
def test_string_hash(api_url, test_string):

  url = f"{api_url}/hash/{test_string}"
  response = requests.get(url)

  print(response.status_code)
  print(response.text)

  if response.status_code == 200:

    data = json.loads(response.text)
    
    import hashlib 
    expected_hash = hashlib.md5(test_string.encode()).hexdigest()
    
    assert data["output"] == expected_hash

  else:
    assert False, "Unexpected response"

def test_invalid_input(api_url):

  url = f"{api_url}/hash/123"
  response = requests.get(url)

  assert response.status_code >= 400
    
# Maya 
# test fibonacci code - Maya
@pytest.mark.parametrize("n,expected,status_code", [
  (6, [1, 1, 2, 3, 5, 8], 200),
  (-1, {"error": "Invalid input"}, 404)  
])
def test_fibonacci(api_url, n, expected, status_code):

  url = f"{api_url}/fibonacci/{n}"
  response = requests.get(url)

  assert response.status_code == status_code
  
  if status_code == 200:
    assert response.json() == expected

  else:
    assert "Not Found" in response.text

def test_invalid_input(api_url):

  url = f"{api_url}/fibonacci/foo"
  response = requests.get(url)
  
# is-prime test function - Maya 
@pytest.mark.parametrize("n,expected", [
  (7, True),
  (10, False),  
  (1, False),
  (-1, False)
])
def test_prime(api_url, n, expected):

  url = f"{api_url}/is-prime/{n}"

  response = requests.get(url)

  if n >= 0:  
    assert response.status_code == 200
    assert response.json()["output"] == expected

  else:
    assert "Not Found" in response.text


def test_prime_invalid_input(api_url):
  
  url = f"{api_url}/is-prime/foo"
  response = requests.get(url)

  assert response.status_code >= 400

# factorial testing - Danny
def test_factorial():
  """Test that the factorial function works correctly for a variety of inputs."""

  # Test positive integers.
  assert factorial(0) == 1
  assert factorial(1) == 1
  assert factorial(5) == 120

  # Test negative integers.
  with pytest.raises(ValueError):
    factorial(-1)

  # Test large numbers.
  assert math.isclose(factorial(100), 9.33262154439441e+157)

  ### Slack Alert Test - Andres ###
@pytest.mark.parametrize("test_message, expected_response",
    [
        ("Test", {"Posted: ": True}),
        ("Test message from testcode.py", {"Posted: ": True}),
    ]
)
def test_slack_alert(api_url, test_message, expected_response):
    webhook_url = os.getenv("SLACK_URL")
    url = f"{api_url}/slack-alert/{test_message}"
    response = requests.get(url)
    assert response.status_code == 200, f"slack_alert endpoint returned a non-200 status code for input: {test_message}"
    actual_response = json.loads(response.text)
    assert actual_response == expected_response, f"slack_alert test failed for input: {test_message}"

@pytest.mark.parametrize("test_message, expected_response",
    [("Failed Test", {"Posted: ": False})]
)
def test_slack_alert_fail(api_url, test_message, expected_response):
    webhook_url = os.getenv("SLACK_URL")
    url = f"{api_url}/slack-alert/{test_message}"
    response = requests.get(url)
    assert response.status_code == 200, f"slack_alert endpoint returned a non-200 status code for input: {test_message}"
    actual_response = json.loads(response.text)
    assert actual_response == expected_response, f"slack_alert test failed for input: {test_message}"