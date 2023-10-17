import requests
import pytest
import math
from math import factorial

@pytest.fixture
def api_url():
  return "http://localhost:8000"

# a function to test the /md5/<string> endpoint
@pytest.mark.parametrize(
    "test_string, expected_md5_hash",
    [
        ("Hello World", "b10a8db164e07541005b7a99be72e3fe5"),
        ("%20", "7215ee9c7d9dc229d2921a40e899ec5f"),
        ("test String", "bd08ba3c982eaad768602536fb8e1184")
    ]
)
def test_md5_endpoint(api_url,test_string,expected_md5_hash):
    url = f"{api_url}/md5/{test_string}"
    response = requests.get(url)
    assert response.status_code == 200, f"MD5 endpoint returned a non-200 status code for input: {test_string}"

    actual_response = json.loads(response.text)
    actual_md5_hash = actual_response['output']

    assert actual_md5_hash == expected_md5_hash, f"MD5 test failed for input: {test_string}"

# Utility function to log the comparison 
def log_comparison(expected, actual, message):
    print(message)
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    
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
