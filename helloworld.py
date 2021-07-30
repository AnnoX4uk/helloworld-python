#!/usr/bin/env python3
from flask import Flask, request
import logging

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        logging.warning('Some point')
        return ('Hello world 1')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
