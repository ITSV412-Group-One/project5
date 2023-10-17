import requests
import sys

URL = "http://localhost:4000"

def test_fibonacci_positive():

  print("Testing /fibonacci positive case...")

  response = requests.get(f"{URL}/fibonacci/6")

  print(response.json())

  assert response.status_code == 200
  assert response.json() == [1, 1, 2, 3, 5, 8]

  print("Positive case passed!")

def test_fibonacci_negative():

  print("Testing /fibonacci negative case...")  

  response = requests.get(f"{URL}/fibonacci/-1")

  print(response.status_code)

  assert response.status_code >= 400
  assert "Invalid input" in response.text
  
  print("Negative case passed!")

if __name__ == "__main__":
  
  test_fibonacci_positive()
  test_fibonacci_negative()

  if True:
    sys.exit(0)
  else: 
    sys.exit(1)