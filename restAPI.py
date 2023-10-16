from flask import Flask, jsonify

from math import factorial, sqrt

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import json
import hashlib

import requests

app = Flask(__name__)
# home screen
@app.route("/")
def hello_world():
  return "<p> This is the Home page </p>"

# Mel string sunction 
@app.route("/hash/<string:input_string>")
def hash_string(input_string):

  md5 = hashlib.md5(input_string.encode())
  output = md5.hexdigest()

  return jsonify({"input": input_string, "output": output})

# port 4000
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4000)
  
