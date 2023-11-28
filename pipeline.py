import click
from flask import Flask, jsonify, request, Response
import random
import hashlib
import os
import requests
import redis
import json
import re
import sys

host = '34.174.43.161'
REDIS = 'redis'

@click.group()
@click.pass_context
@click.option('--user-key', default='', help='Command Line Interface')
def cli(ctx, user_key):
    ctx.obj['user_key'] = user_key

@cli.command('md5')
@click.pass_context
@click.option('--word', default='hello', help='md5 command')
def md5(ctx, word):
    hash_obj = hashlib.md5(word.encode())
    return jsonify(input=word, output=hash_obj.hexdigest())

@cli.command('factorial')
@click.pass_context
@click.option('--n', default='1', help='factorial test')
def is_factorial(ctx, n):
    n = int(n)
    factorial = 1
    if n < 0:
        return f"The number {n} is not a positive integer"
    elif n == 0:
        return jsonify(input=n, output=1)
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        return jsonify(input=n, output=factorial)

@cli.command('fibonacci')
@click.pass_context
@click.option('--n', default='1', help='fibonacci test')
def fibonacci_num(ctx, n):
    fibonacci = [0]
    a, b = 0, 1
    while b <= n:
        fibonacci.append(b)
        a, b = b, a + b
    return jsonify(input=n, output=fibonacci)

@cli.command('prime-check')
@click.pass_context
@click.option('--n', default='1', help='is-prime test')
def prime_check(ctx, n):
    n = int(n)
    if n < 0:
        return f"Enter a positive non-zero integer"
    elif n == 2:
        return jsonify(input=n, output=True)
    elif n == 1 or n == 15:
        return jsonify(input=n, output=False)
    else:
        for i in range(2, n):
            if n % i == 0:
                return jsonify(input=n, output=False)
        return jsonify(input=n, output=True)

@cli.command('slack-alert')
@click.pass_context
@click.option('--msg', default='1', help='slack-alert test')
def post_to_slack(ctx, msg):
    SLACK_URL = 'https://hooks.slack.com/services/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'
    data = {'text': msg}
    resp = requests.post(SLACK_URL, json=data)
    if resp.status_code == 200:
        result = True
        mesg = "Message successfully posted to Slack channel"
    else:
        result = False
        mesg = f"There was a problem posting to the Slack channel (HTTP response: {resp.status_code})."
    return jsonify(input=msg, output=result, message=mesg), 200 if resp.status_code == 200 else 400

# Add your other commands here...

if __name__ == '__main__':
    cli(obj={})