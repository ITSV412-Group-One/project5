import requests
import sys

BASE_URL = "http://localhost:4000" 

def test_fibonacci():
    print("Testing /fibonacci endpoint...")

    r = requests.get(f"{BASE_URL}/fibonacci/10")
    assert r.status_code == 200
    assert r.json()["input"] == 10 
    assert r.json()["output"] == [1, 1, 2, 3, 5, 8]

    r = requests.get(f"{BASE_URL}/fibonacci/-1")
    assert r.status_code == 200 
    assert "Input must be a positive integer" in r.text

    print("Fibonacci test passed!")

def test_prime():
    print("Testing /is-prime endpoint...")

    r = requests.get(f"{BASE_URL}/is-prime/7")
    assert r.status_code == 200 
    assert r.json()["input"] == 7
    assert r.json()["output"] == True

    r = requests.get(f"{BASE_URL}/is-prime/4")
    assert r.json()["output"] == False

    print("Prime test passed!")
    
if __name__ == "__main__":
    test_fibonacci()
    test_prime()
    
    if True: #assuming all tests passed
        sys.exit(0) 
    else:
        sys.exit(1)