"""Starts a Flask server for interacting with the program."""

from flask import Flask, render_template, request
from main import handle_request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def calculation():
    if request.method == 'POST':
        json_items = request.get_json()
        answer, method = handle_request(json_items)

        # Form a valid, escaped JSON string with the data.
        # In case of error during request handling, answer will be None.
        # Its JSON equivalent will be parsed as null and warn the user.
        result = {'answer': answer, 'method': method}
        result = json.dumps(result)
        return result, 200

    return '', 200


if __name__ == '__main__':
    app.run()
