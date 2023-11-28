# rest api 
from flask import Flask, jsonify, request
import redis
import re
import sys


from math import factorial, sqrt
import json
import hashlib
import requests
import traceback


#from slack_sdk import WebClient
#from slack_sdk.errors import SlackApiError
# For Slack-Alert Function. 
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PWD = os.getenv('REDIS_PWD')
redis_client = redis.Redis(
  host=REDIS_HOST, 
  port=REDIS_PORT,
  password=REDIS_PWD,
  decode_responses=True
)

@app.route('/keyval', methods = ['POST'])
def post():
	"""
	Insert a single entry into the database.
	:param key: The key for the entry.
	:type key: string
	:param value: The associated value.
	:return: True is the insertion was successful; False otherwise.
	:rtype: bool
	"""
	payload = request.get_json()
	
	
	if REDIS.exists(payload['key']):
		
		return jsonify(
			key= payload['key'], 
			value = payload['value'], 
			command=f"CREATE {payload['key']}/{payload['value']}",
			result=False, 
			error="Key already exists"
		), 409
	else:	
		REDIS.set(payload['key'], payload['value'])
		return jsonify(
			key= payload['key'], 
			value = payload['value'], 
			command=f"CREATE {payload['key']}/{payload['value']}",
			result=True, 
			error=""
		), 200


@app.route('/keyval/<string:user_key>', methods = ['GET'])
def get(user_key):
	"""
	Returns the entry associated with the key.
	:param key: the key of the entry to be retrieved from the database
	:type key: string
	:return: entry associated with that key
	:rtype: KeyValue"""
	
	
	if REDIS.exists(user_key):
		redis_val = REDIS.get(user_key)
		return jsonify(
			key=user_key,
			value=redis_val.decode('unicode-escape'), #decodes the byte string to python string
			command=f"GET {user_key}",
			result=True,
			error= ""
		), 200
	else:
		return jsonify(
			key=user_key, 
			value=None, 
			command=f"GET {user_key}",
			result=False, 
			error="Key does not exist"
		), 404
	
@app.route('/keyval', methods = ['PUT'])
def put():
	"""
	Updates the entry associated with the key with the value provided.
	:param key: the entry's key
	:param value: the new value of the entry
	:return: void
	"""
	
	payload = request.get_json()
	
	if REDIS.exists(payload['key']):
		REDIS.set(payload['key'], payload['value'])
		return jsonify(
			key= payload['key'], 
			value=payload['value'], 
			command=f"UPDATE {payload['key']}/{payload['value']}",
			result=True, 
			error=""
		), 200
	else:
		return jsonify(
			key= payload['key'], 
			value = payload['value'], 
			command=f"UPDATE {payload['key']}/{payload['value']}",
			result=False, 
			error="Key does not exist, use POST to create key value pair."
		), 404

@app.route('/keyval/<string:user_key>',methods = ['DELETE'])
def delete(user_key):
	"""
	Remove the entries associate with the keys provided.
	:param keys: The keys of the entries to remove
	:type keys: List<string>
	:return: void
	"""
	
	if REDIS.exists(user_key):	
		redis_val = REDIS.get(user_key)
		REDIS.delete(user_key)
		return jsonify(
			key=user_key,
			value=redis_val.decode('unicode-escape'), #decodes the byte string to python string
			command=f"DELETE {user_key}",
			result=True,
			error= ""
		), 200
	else:
		return jsonify(
			key=user_key, 
			value=None, 
			command=f"DELETE {user_key}",
			result=False, 
			error="Key does not exist, use POST to create key value pair."
		), 404
  
# home screen
@app.route("/")
def hello_world():
  return "<p> Welcome Page! </p>"

# Mel string sunction 
@app.route("/md5/<string:input_string>")
def md5_string(input_string):

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
def fibonacci_num(n):
	fibonacci = [0]
	a = 0
	b = 1
	fib = 0
	check = 0

	if n < 0:
        	return jsonify(input=n, output="Error: Input must be a positive integer")
	elif n == 0:
        	fibonacci = [0]
	else:
		while b <= n:
			fibonacci.append(b)
			a , b = b, a + b
	return jsonify(input=n, output=fibonacci)
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
  

# Slack Function - Andres
@app.route("/slack-alert/<string:message>")
def slack_alert(message):
	webhook_url = os.getenv("SLACK_URL")
	response = requests.post(webhook_url, json={"text": message})

  # This checks if 
	if response.status_code == 200:
		return jsonify({"Posted: ": True})
	else:
		return jsonify({"Posted: ": False})

@app.route("/tests")
def run_tests():
    testcode.test_string_hash() 
    testcode.test_fibonacci()
    testcode.test_prime()
    testcode.test_factorial()
    testcode.test_slack_alert()
    
    return "Tests passed"

# port 4000
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4000)
  
  run_tests()
  
