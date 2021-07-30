#!/usr/bin/env python3
from flask import Flask, request
import sys

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        sys.stdout('This is a point')
        return ('Hello world 1')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
