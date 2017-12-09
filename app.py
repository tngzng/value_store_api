import json

from flask import Flask
from flask import request


app = Flask(__name__)


class ValueStore:
    def __init__(self):
        self._store = {}

    def set(self, key, val):
        self._store[key] = val

    def get(self, key):
        return self._store.get(key, None)


value_store = ValueStore()


@app.route('/')
def root():
    return 'OK'


@app.route('/health')
def health():
    return 'OK'


@app.route('/set')
def set():
    count = 0
    for key, val in request.args.items():
        value_store.set(key, val)
        count += 1

    response = {'count': count}
    return json.dumps(response)


@app.route('/get')
def get():
    keys = request.args.get('keys')
    # raise 404 for missing keys arg
    key_arr = keys.split(',')
    response = {}
    for key in key_arr:
        response[key] = value_store.get(key)

    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
