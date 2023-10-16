import requests
import sys

BASE_URL = "http://localhost:4000" 

def test_fibonacci():
  print("Testing /fibonacci endpoint...")

  r = requests.get(f"{BASE_URL}/fibonacci/10")
  
  print(f"Status code: {r.status_code}")
  print(f"Response: {r.text}")
  
  assert r.status_code == 200
  assert r.json()["input"] == 10
  assert r.json()["output"] == [1, 1, 2, 3, 5, 8]

  r = requests.get(f"{BASE_URL}/fibonacci/-1")
  
  print(f"Status code: {r.status_code}")
  print(f"Response: {r.text}")
  
  assert r.status_code == 200
  assert "Input must be positive" in r.text

  print("Fibonacci test passed!")

if __name__ == "__main__":
  test_fibonacci()

  if True: 
    sys.exit(0)
  else:
    sys.exit(1)