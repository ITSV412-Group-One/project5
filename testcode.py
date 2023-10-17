import requests

URL = "http://localhost:4000"

def test_fibonacci_positive():
  print("Testing /fibonacci endpoint...")
  response = requests.get(f"{URL}/fibonacci/6")
  assert response.status_code == 200
  assert response.json() == [1, 1, 2, 3, 5]
  
  print(f"Status code: {r.status_code}")
  print(f"Response: {r.text}")

def test_fibonacci_negative():
  print("Testing /fibonacci endpoint...")
  response = requests.get(f"{URL}/fibonacci/-1") 
  assert response.status_code == 400
  
  print(f"Status code: {r.status_code}")
  print(f"Response: {r.text}")
  
  if __name__ == "__main__":
    test_fibonacci_positive()
    test_fibonacci_negative()

  if True:
    sys.exit(0)
  else:
    sys.exit(1)