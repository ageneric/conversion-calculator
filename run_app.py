"""Starts a Flask server for interacting with the program."""

from flask import Flask, render_template, request
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def calculation():
    if request.method == 'POST':
        json_items = request.get_json()

        try:
            steps = parse_request(json_items)
            answer, method = evaluate_steps(steps)
        except Exception as generic_error:
            print(generic_error)
            answer, method = 'null', 'Error: ' + str(generic_error)

        # Escape all strings. Cannot use single quotes, as JSON
        # will only accept double quotes / escaped double quotes.
        # TODO: switch to json module (None -> "null", escape quotes).
        method = str(method).replace('"', r'\"').replace('\'', r'"')
        result = f'"answer": "{answer}", "method": "{method}"'
        result = '{' + result + '}'  # Format for JSON parsing.
        return result, 200

    return '', 200


if __name__ == '__main__':
    app.run()
