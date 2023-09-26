from flask import Flask, jsonify

from math import factorial, sqrt

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import json
import hashlib

from flask import Flask


# Mel string sunction 
string = str(input("Enter a sting of characteristics: "))
md5 = hashlib.md5(string.encode())
end_md5 = md5.hexdigest()

#endpoint
json_obj =  {
  "input": string,
  "output": end_md5
}

#convert to JSON:
final_obj = json.dumps(json_obj)

print(final_obj)


app = Flask(__name__)

# home screen
@app.route("/")
def hello_world():
  return "<p> This is the Home page </p>"

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

# Maya 
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
  
