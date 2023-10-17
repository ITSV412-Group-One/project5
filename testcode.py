import requests

URL = "http://localhost:4000"

def test_fibonacci_positive():
  response = requests.get(f"{URL}/fibonacci/6")
  assert response.status_code == 200
  assert response.json() == [1, 1, 2, 3, 5]

def test_fibonacci_negative():
  response = requests.get(f"{URL}/fibonacci/-1") 
  assert response.status_code == 400