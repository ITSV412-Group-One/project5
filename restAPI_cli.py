import os
import argparse
import requests 
import json
import sys

if os.environ.get('DOCKER_NETWORK_MODE') == 'backend':
  BASE_URL = 'http://restapi:4000'
else:
  BASE_URL = 'http://127.0.0.1:8000' 

parser = argparse.ArgumentParser(description='CLI for API')
parser.add_argument('command')
parser.add_argument('args', nargs='?')

def call_api(endpoint, args):

  print(f"Command: {command}, Args: {args}")

  url = BASE_URL + '/' + endpoint
  print(f"Request URL: {url}")

  if args:
    resp = requests.post(url, json=args)
  else:
    resp = requests.get(url)

  # Rest of function

if __name__ == '__main__':
  
  args = parser.parse_args()
  command = args.command
  command_args = args.args

  print("Testing hardcoded endpoint...")
  call_api("users", None)

  print("Calling command endpoint")
  call_api(command, command_args)