# rest api 
from flask import Flask, jsonify, request
import redis

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

#Danny GET function
@app.route('/keyval/<string:key>', methods=['GET'])
def get_key_value(key):
    try:
        value = redis_client.get(key)
        if value is not None:
            return jsonify({'key': key, 'value': value.decode()}), 200
        else:
            return jsonify({'error': 'Key does not exist'}), 404
    except Exception as e:
        return jsonify({'error': 'Invalid request', 'message': str(e)}), 400

# Maya 
def fibonacci(n):
  if n < 0: 
    return "Error: Input must be >= 0"

  sequence = [1, 1]

  if n == 0:
    return sequence[0]
  elif n == 1: 
    return sequence[1]
  else:
    for i in range(2, n+1):
      next_num = sequence[-1] + sequence[-2]
      sequence.append(next_num)

  return sequence[-1]

@app.route("/fibonacci/<int:n>")
def get_fibonacci(n):

  result = fibonacci(n)

  return jsonify({
     "input": n,
     "output": result
  })

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
  
#Create function - Maya 
@app.route('/keyval', methods=['POST'])
def create_keyval():
    data = request.get_json()
    
    if not data or not 'key' in data or not 'value' in data:
        return jsonify({'error': 'Invalid request, key and value required'}), 400
    
    key = data['key']
    value = data['value']
    
    if redis_client.exists(key):
        return jsonify({
            'error': f'Key {key} already exists'
        }), 409
        
    redis_client.set(key, value)
    return jsonify({
        'key': key, 
        'value': value,
        'result': True
    })

# Update
@app.route('/keyval', methods=['PUT'])
def update_keyval():
    data = request.get_json()
    key = data.get('storage-key')
    value = data.get('storage-val')  

    if not key or not value:
        return jsonify({
            'error': 'Invalid request. Both "storage-key" and "storage-val" must be provided.'
        }), 400

    if not redis_client.exists(key):
        return jsonify({
            'error': f'Key {key} does not exist'
        }), 404

    redis_client.set(key, value)
    return jsonify({
        'key': key,
        'value': value,
        'result': True
    }), 200

# Delete
@app.route('/keyval/<string:key>', methods=['DELETE'])
def delete_keyval(key):
    if not redis_client.exists(key):
        return jsonify({
            'error': f'Key {key} does not exist'
        }), 404
    else:
      redis_client.delete(key)
    return jsonify({
        'message': f'Key {key} deleted successfully'
    }), 200

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

# port 4000
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4000)
  
