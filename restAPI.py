from flask import Flask, jsonify

from math import factorial, sqrt

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import json
import hashlib

import requests
import traceback

app = Flask(__name__)
# home screen
@app.route("/")
def hello_world():
  return "<p> Welcome Page! </p>"

# Mel string sunction 

import json
import requests


base_url = "http://127.0.0.1:4000"


def log_comparison(expected, actual, message):
   print(f"Expected: {expected}")
   print(f"Actual: {actual}")
   assert expected == actual, message 


# a function to test the /md5/<string> endpoint
def test_md5_endpoint():
   test_cases = [
      ("Hello World", "b10a8db164e07541005b7a99be72e3fe5"),
      ("%20", "7215ee9c7d9dc229d2921a40e899ec5f"),
      ("test String", "bd08ba3c982eaad768602536fb8e1184")
   ]

   for test_string, expected_md5_hash in test_cases:
      url = f"{base_url}/md5/{test_string}"
      response = requests.get(url)
      if response.status_code != 200:
         print(f"MD5 endpoint returned a non-200 status code for input: {test_string}")
         continue  # skip to the next test case

      actaul_response = json.loads(response.text)
      actual_md5_hash = actaul_response['output']

      if actual_md5_hash == expected_md5_hash:
         print(f"MD5 test passed for input: {test_string}")
      else:
         print(f"MD5 test failed for input: {test_string}")
         log_comparison(expected_md5_hash, actual_md5_hash, "MD5 hash does not match")

#Danny
# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#factorial result
@app.route('/factorial/<int:num>', methods=['GET'])
def calculate_factorial(num):
    if num < 0:
        return jsonify({'error': 'Factorial is not defined for negative numbers'})
    result = factorial(num)
    return jsonify({'input': num, 'output': result})
  
# Maya 
@app.route("/fibonacci/<int:n>")
def fibonacci(n):
  try:
    if n < 0:
      raise ValueError("Invalid input")  

    # positive case logic
    sequence = [1, 1]

    i = 2
    while i < n:
      next_val = sequence[-1] + sequence[-2]
      sequence.append(next_val)
      i += 1
    
    return jsonify(sequence)

  except ValueError as e:
    return str(e), 400

  except Exception as e:
    return "Error", 500

# Maya 
def is_prime(num):
  if num <= 1:
    return False

  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  
  return True

@app.route("/is-prime/<int:input_number>")
def check_prime(input_number):

  result = is_prime(input_number)

  return jsonify({
    "input": input_number, 
    "output": result
  })
  

# port 4000
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4000)
  
