import os
import argparse
import requests 
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('arg', nargs='?')
args = parser.parse_args()

command = args.command
arg = args.arg

if os.environ.get('DOCKER_NETWORK_MODE') == 'backend':
  BASE_URL = 'http://restapi:4000'  
else:
  BASE_URL = 'http://127.0.0.1:8000'

def call_api(endpoint):
  
  url = BASE_URL + '/' + endpoint
  
  print(f'Calling API: {url}')

  resp = requests.get(url)

  if resp.status_code == 200:
    print(resp.json())
  else:
    print(f'Error: {resp.status_code}')


if __name__ == '__main__':

  # Test hardcoded endpoints
  print('Testing endpoints...')

  call_api('md5/hello')
  call_api('factorial/5')
  call_api('fibonacci/5')
  call_api('is-prime/7')

  if arg:
    endpoint = f'{command}/{arg}'
  else:
    endpoint = command
  
  print(f'Calling endpoint: {endpoint}')

  call_api(endpoint)