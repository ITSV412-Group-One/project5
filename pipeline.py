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
    click.echo(f"Input: {word}, Output: {hash_obj.hexdigest()}")

@cli.command('factorial')
@click.pass_context
@click.option('--n', default='1', help='factorial test')
def is_factorial(ctx, n):
    n = int(n)
    factorial = 1
    if n < 0:
        click.echo(f"The number {n} is not a positive integer")
    elif n == 0:
        click.echo(f"Input: {n}, Output: 1")
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        click.echo(f"Input: {n}, Output: {factorial}")

@cli.command('fibonacci')
@click.pass_context
@click.option('--n', default='1', help='fibonacci test')
def fibonacci_num(ctx, n):
    fibonacci = [0]
    a, b = 0, 1
    while b <= int(n):
        fibonacci.append(b)
        a, b = b, a + b
    click.echo(f"Input: {n}, Output: {fibonacci}")

@cli.command('prime-check')
@click.pass_context
@click.option('--n', default='1', help='is-prime test')
def prime_check(ctx, n):
    n = int(n)
    if n < 0:
        click.echo(f"Enter a positive non-zero integer")
    elif n == 2:
        click.echo(f"Input: {n}, Output: True")
    elif n == 1 or n == 15:
        click.echo(f"Input: {n}, Output: False")
    else:
        for i in range(2, n):
            if n % i == 0:
                click.echo(f"Input: {n}, Output: False")
                break
        else:
            click.echo(f"Input: {n}, Output: True")

@cli.command('slack-alert')
@click.pass_context
@click.option('--msg', default='1', help='slack-alert test')
def post_to_slack(ctx, msg):
    SLACK_URL =  "https://hooks.slack.com/services/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"
    data = {'text': msg}
    resp = requests.post(SLACK_URL, json=data)
    if resp.status_code == 200:
        result = True
        mesg = "Message successfully posted to Slack channel"
    else:
        result = False
        mesg = f"There was a problem posting to the Slack channel (HTTP response: {resp.status_code})."
    click.echo(f"Input: {msg}, Output: {result}, Message: {mesg}")

if __name__ == '__main__':
    cli(obj={})