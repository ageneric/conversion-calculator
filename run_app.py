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
            steps = parse_method(json_items)
            result = run_method(steps)
        except Exception as generic_error:  # Generic error catcher.
            print(generic_error)
            result = 'Error: ' + str(generic_error)

        return f'{result}', 200

    return '', 200


if __name__ == '__main__':
    app.run()
