import requests
import json
from flask import Flask, jsonify, escape, request, Response
host = '34.174.43.161'
errors = 0

#!/usr/bin/env python

all_tests_dict = {  #all endpoints and expected results
    '/md5/test': '098f6bcd4621d373cade4e832627b4f6',
    '/md5/hello%20world': '5eb63bbbe01eeed093cb22bb8f5acdc3',
    '/md5': 404,
    '/factorial/4': 24,
    '/factorial/5': 120,
    '/factorial/test': 404,
    '/fibonacci/0':[0],
    '/fibonacci/8':[0,1,1,2,3,5,8],
    '/fibonacci/35':[0,1,1,2,3,5,8,13,21,34],
    '/fibonacci/1':[0,1,1],
    '/fibonacci/test': 404,
    '/is-prime/1': False,
    '/is-prime/2': True,
    '/is-prime/5': True,
    '/is-prime/6': False,
    '/is-prime/15': False,
    '/is-prime/37': True,
    '/is-prime/one': 404,
    '/slack-alert/test': True,
    '/slack-alert/this%20is%20a': True
    }
keyval_tests_dict = {
    '/keyval' : {'key':'test1', 'value':'1'}
    
    }

        
for path, result in all_tests_dict.items(): 
    print(f"Path: {path} / EXPECTED RESULT: {result}")
    t = requests.get(f'http://{host}{path}')
    if t.status_code == 200:
        print(f"Actual Result: {t.json()['output']}")
        if t.json()['output'] == result:
            print("PASS\n")
        else:
            print("ERROR\n")
            errors += 1
            
    elif t.status_code == 404:
        
        if result == 404:
            print("PASS\n")
        else:
            print("ERROR\n")
            errors += 1
    else:
            print("ERROR\n")
            errors += 1
    
              
for path, result in keyval_tests_dict.items(): #post
    print(f"Path: {path} / Method: POST / json payload {result}")
    t = requests.post(f'http://{host}{path}', json=result)
    print(t.status_code)
    if t.status_code == 200:
        print("PASS\n")
    else:
        print("ERROR\n")
        errors += 1
 

              
for path, result in keyval_tests_dict.items(): #GET
    print(f"Path: {path} / Method: GET / json payload {result}")
    t = requests.get(f'http://{host}{path}/test1') # hardcoded get string. Could string splice my Dict key to extract the key string
    print(f"Status code: {t.status_code}")
    if t.status_code == 200:
        print("PASS\n")
    else:
        print("ERROR\n")
        errors += 1       
              
for path, result in keyval_tests_dict.items(): #PUT
    print(f"Path: {path} / Method: PUT / json payload 'key':'test1', 'value':'something'")
    t = requests.put(f'http://{host}{path}', json={'key':'test1', 'value':'something'})
    print(f"Status code: {t.status_code}")
    if t.status_code == 200:
        print("PASS\n")
    else:
        print("ERROR\n")
        errors += 1       
              
for path, result in keyval_tests_dict.items(): #DELETE
    print(f"Path: {path} / Method: DELETE / json payload 'key':'test1', 'value':'something'")
    t = requests.delete(f'http://{host}{path}/test1')
    print(f"Status code: {t.status_code}")
    if t.status_code == 200:
        print("PASS\n")
    else:
        print("ERROR\n")
        errors += 1                     
             

              

              
print(f"Errors = {errors}")