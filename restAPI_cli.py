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
  url = BASE_URL + '/' + endpoint
  if args:
    resp = requests.post(url, json=args)
  else:
    resp = requests.get(url)

  if resp.status_code != 200:
    print(f"Error: {resp.status_code}")
    return

  data = resp.json()
  print(json.dumps(data, indent=2))

if __name__ == '__main__':
  args = parser.parse_args()
  command = args.command
  command_args = args.args

  call_api(command, command_args)