import requests
import pytest
from requests import codespi

BASE_URL = "http://localhost:4000"

def test_fibonacci():

  # Positive test
  response = requests.get(f"{BASE_URL}/fibonacci/10")
  assert response.status_code == codes.ok
  assert response.json()["input"] == 10
  assert response.json()["output"] == [1, 1, 2, 3, 5, 8]

  # Negative test
  response = requests.get(f"{BASE_URL}/fibonacci/-1")
  assert response.status_code == codes.bad_request
  assert "Input must be positive" in response.json()["error"]

  # Edge case
  response = requests.get(f"{BASE_URL}/fibonacci/0")
  assert response.json()["output"] == []

  # Invalid input type
  response = requests.get(f"{BASE_URL}/fibonacci/foo")
  assert response.status_code == codes.bad_request

  print("Fibonacci tests passed!")

# Additional test functions for each endpoint

def run_tests():
  functions = [test_fibonacci] # etc

  for test in functions:
    test()

  # Return 0 if all passed
  return 0

if __name__ == "__main__":
  exit_code = run_tests()
  sys.exit(exit_code)