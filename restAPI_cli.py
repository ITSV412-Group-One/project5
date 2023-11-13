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
  
  resp = requests.get(url)

  if resp.status_code == 200:
    data = resp.json()
    print(json.dumps(data, indent=2))
  else:
    print(f'Error: {resp.status_code}')

  # Rest of function

if __name__ == '__main__':
  
  args = parser.parse_args()
  
  command = args.command
  command_args = args.args

  # Test hardcoded endpoint
  print('Testing hardcoded endpoint...')
  call_api('hash/hello')
  call_api('factorial/5') 
  call_api('hash/hello')
  call_api('fibonacci/5')
  call_api('is-prime/5')

  if arg:
    endpoint = f'{command}/{arg}'
  else:
    endpoint = command  

  print(f'Calling endpoint: {endpoint}')

  # Call API with endpoint
  call_api(endpoint)