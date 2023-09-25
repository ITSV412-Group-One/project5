from flask import Flask, jsonify

from math import factorial, sqrt

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


import hashlib

app = Flask(__name__)

@app.route("/fibonacci/<int:input_number>")
def get_fibonacci(input_number):

  # Check for valid input
  if input_number <= 0: 
    return "Input must be a positive integer"

  sequence = []

  # Generate Fibonacci sequence
  a, b = 0, 1
  while b < input_number:
    sequence.append(b)
    a, b = b, a+b

  return jsonify({
    "input": input_number,
    "output": sequence
  })
  
 # Is prime function 
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