import json

from flask import Flask
from flask import request
from flask import abort


app = Flask(__name__)
DATA_STORE_FILEPATH = 'data_store/data_store.json'


class ValueStore:
    def set(self, key, val):
        with open(DATA_STORE_FILEPATH, 'r+') as data_store:
            try:
                loaded_data_store = json.load(data_store)
            except ValueError:
                loaded_data_store = {}
            loaded_data_store[key] = val
            data_store.seek(0)
            json.dump(loaded_data_store, data_store)

    def get(self, key):
        with open(DATA_STORE_FILEPATH, 'r') as data_store:
            try:
                loaded_data_store = json.load(data_store)
            except ValueError:
                loaded_data_store = {}
            return loaded_data_store.get(key, None)


value_store = ValueStore()


@app.route('/')
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
    if not keys:
        abort(404, 'keys is a required param')
    key_arr = keys.split(',')
    response = {}
    for key in key_arr:
        response[key] = value_store.get(key)

    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
