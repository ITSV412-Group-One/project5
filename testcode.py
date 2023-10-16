import requests
import sys

BASE_URL = "http://localhost:4000" 

def test_fibonacci():
    print("Testing /fibonacci endpoint...")
    r = requests.get(f"{BASE_URL}/fibonacci/10")
    data = r.json()
    
    assert r.status_code == 200 
    assert data["input"] == 10
    assert data["output"] == [1, 1, 2, 3, 5, 8]
    
    print("Fibonacci test passed!")
