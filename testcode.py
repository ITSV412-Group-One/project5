import requests
import pytest

@pytest.fixture
def api_url():
  return "http://localhost:5000"

@pytest.mark.parametrize("n,expected", [
  (6, [1, 1, 2, 3, 5, 8]),
  (-1, {"error": "Invalid input"})  
])
def test_fibonacci(api_url, n, expected):

  url = f"{api_url}/fibonacci/{n}"
  response = requests.get(url)

  assert response.status_code == 200
  assert response.json() == expected

def test_invalid_input(api_url):

  url = f"{api_url}/fibonacci/foo"
  response = requests.get(url)