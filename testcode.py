import requests
from requests import codes

BASE_URL = "http://localhost:4000"

def test_fibonacci():

  print("Testing /fibonacci endpoint...")

  # Positive case
  r = requests.get(f"{BASE_URL}/fibonacci/10")
  
  assert r.status_code == codes.ok 
  assert r.json()["input"] == 10
  assert r.json()["output"] == [1, 1, 2, 3, 5, 8]

  # Negative case  
  r = requests.get(f"{BASE_URL}/fibonacci/-1")

  assert r.status_code == codes.bad_request
  assert "Input must be positive" in r.json()["error"]

  # Edge case
  r = requests.get(f"{BASE_URL}/fibonacci/0")  

  assert r.status_code == codes.ok
  assert r.json()["output"] == []

  print("Fibonacci test passed!")


if __name__ == "__main__":
  
  test_fibonacci()

  if True:
    sys.exit(0)
  else:
    sys.exit(1)