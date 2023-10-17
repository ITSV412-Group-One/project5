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
  return "<p> This is the Home page </p>"

# port 4000
port = 4000

if __name__ == "__main__": 
  print("App starting on port {}".format(port))
  app.run(host='0.0.0.0', port=4000)
  
