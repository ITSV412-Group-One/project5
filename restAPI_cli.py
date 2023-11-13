import argparse
import requests 
import json
import sys

BASE_URL = 'http://127.0.0.1:4000' 

parser = argparse.ArgumentParser(description='Command line client for Example API')
parser.add_argument('command', help='API command to run')
parser.add_argument('args', nargs='?', default=[], help='Arguments for command')

def call_api(endpoint, args):
    url = BASE_URL + '/' + endpoint
    if args:
        resp = requests.post(url, json=args) 
    else:
        resp = requests.get(url)
    
    if resp.status_code != 200:
        print(f'Error: API request failed with status {resp.status_code}', file=sys.stderr)
        return
        
    data = resp.json()
    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    args = parser.parse_args()
    command = args.command
    command_args = args.args
    call_api(command, command_args)