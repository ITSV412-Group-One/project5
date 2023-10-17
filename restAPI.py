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
@app.route("/hash/<string:input_string>")
def hash_string(input_string):

  md5 = hashlib.md5(input_string.encode())
  output = md5.hexdigest()

  return jsonify({"input": input_string, "output": output})

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
  
