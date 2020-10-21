"""Starts a Flask server for interacting with the program."""

from flask import Flask, render_template, request
from main import valid_base
from digit import DigitCollection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def calculation():
    if request.method == 'POST':
        json_items = request.get_json()
        return f'{json_items}', 200

    return '', 200

if __name__ == '__main__':
    app.run()
