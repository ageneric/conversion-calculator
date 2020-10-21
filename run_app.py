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
        result = parse_method(json_items)
        return f'{result}', 200

    return '', 200

def parse_method(json_items):
    raw_method = []

    try:
        steps = json_items['items']
        for step in steps:
            if step['type'] == 'value':
                base, wrap_point = valid_base(step['base'])
                value = int(step['numeric'])
                new = DigitCollection.init_from_value(value, base, wrap_point)
                raw_method.append(new)
            elif step['type'] == 'calculation':
                raw_method.append(step['calc'])
            else:
                raise ValueError('Invalid request.')

        return raw_method
    except Exception as e:  # Generic error catcher.
        print(e, e.__traceback__, sep="\n")
        return e


if __name__ == '__main__':
    app.run()
