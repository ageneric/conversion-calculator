"""Demonstrates conversions between bases
and number representation systems.

Task 1.4.1.f Kevin Gao
"""

from constants import *
from digit import DigitCollection
import working


def parse_request(json_items):
    """Get a JSON-style structure: an array of Dict (str -> str)
    like {'type': 'value', ...} representing each step requested.
    Attempt to parse instructions from it."""
    raw_method = []

    try:
        for step in json_items:
            if step['type'] == 'value':
                new_base, new_wrap_point = valid_base(step['base'])
                new_digits, new_polarity = parse_numeric(step['numeric'])

                new = DigitCollection(new_digits, new_polarity, new_base, new_wrap_point)
                raw_method.append(new)
            elif step['type'] == 'calculation':
                calc = step['calc'].lower()
                if calc in conversions:
                    raw_method.append((CONVERSION, valid_base(calc)))
                elif calc in functions:
                    raw_method.append((FUNCTION, calc))
                else:
                    raise ValueError('Unknown calculation.')
            else:
                raise ValueError('Invalid request.')

        return raw_method
    except KeyError:
        raise KeyError('Failed to parse steps - key not found.')

def valid_base(user_input: str):
    lowercase_input = user_input.lower()
    
    if lowercase_input in name_binary:
        return BINARY, BINARY
    elif lowercase_input in name_octal:
        return OCTAL, OCTAL
    elif lowercase_input in name_decimal:
        return DECIMAL, DECIMAL
    elif lowercase_input in name_hexadecimal:
        return HEXADECIMAL, HEXADECIMAL
    elif lowercase_input in name_bcd:
        return DECIMAL, HEXADECIMAL

    raise ValueError('Invalid base: base not found. Accepted bases include \
binary, octal, decimal and hexadecimal (and bcd).')

def parse_numeric(numeric: str):
    """Convert digits represented as a single numeral string
    into individual integer digits."""
    if numeric[0] == '-':
        polarity = 1
        numeric = numeric.lstrip('-')
        numeric = numeric.lstrip('0')
    else:
        polarity = 0

    digits = []
    for character in numeric:
        try:
            digits.append(int(character, 10))
        except ValueError:
            # (Bases 11 - 16) Hexadecimal replacement characters.
            if character in inv_extended_numerals.keys():
                digits.append(inv_extended_numerals[character.lower()])
            else:
                raise ValueError('Invalid numeric string. Can only use digits \
0 through 9 and hexadecimal a through f.')

    if len(digits) < 1:
        raise ValueError('Invalid numeric string. Must supply at least one digit.')
    else:
        return digits, polarity

def step_type(step):
    if isinstance(step, DigitCollection):
        return NEW_NUMBER

    try:
        return step[0]
    except TypeError:
        raise TypeError(f'Could not parse the type of step: {step}.')

def digit_method_value(memory, f_name):
    """Execute a single method of the DigitCollection
    (held in variable 'memory') and return its value."""

    if f_name == functions[1]:
        return memory.numeral()
    elif f_name == functions[2]:
        return memory.value()
    elif f_name == functions[3]:
        return memory.pad_to_bytes()
    elif f_name == functions[4]:
        return memory.one_complement()
    elif f_name == functions[5]:
        return memory.two_complement()
    elif f_name == functions[6]:
        return memory.sign_and_magnitude()

def evaluate_steps(steps):
    """Runs through a list of steps sanitised
    in parse_request() and attempts to execute
    the request's instructions & return working."""
    working.clear()
    working.working = []

    if step_type(steps[0]) != NEW_NUMBER:
        raise ValueError('The list of steps must start with a number.')

    memory = None
    operation = None
    representations = []

    for current_step in steps:
        working.current_step = []

        _step_type = step_type(current_step)
        if _step_type == NEW_NUMBER:
            if operation is None:
                working.log_method('Overwritten stored number', current_step, priority_level=2)
                memory = current_step
            elif operation == functions[0]:
                working.log_method('Addition', memory, current_step, priority_level=2)
                memory = memory + current_step
                operation = None
            else:
                raise ValueError(f'Unknown operation during steps execution {operation}.')

        elif _step_type == CONVERSION:
            conversion_types = current_step[1]
            working.log_method('Conversion', conversion_types, priority_level=2)
            memory = memory.convert_base(conversion_types[0], conversion_types[1])

        elif _step_type == FUNCTION:
            f_name = current_step[1]
            if f_name == functions[0]:
                working.log_method('Add the next value supplied', priority_level=2)
                operation = f_name
            else:
                working.log_method('Display', f_name, priority_level=2)
                x = digit_method_value(f_name)
                representations.append(x)
                working.log_method('Representation: Result', x, priority_level=1)

        # If any working has been added to the log during the step.
        if working.current_step:
            working.working.append(working.current_step)

    if step_type(memory) == NEW_NUMBER:
        answer = str(memory)
    else:
        raise ValueError('Corrupted memory during steps execution.')

    method = '<div>' + '</div><div>'.join(working.working) + '</div>'
    return answer, method


if __name__ == '__main__':
    print("""* It is preferred to use the Flask web app included, by running
run_app.py with Flask - but if that is not possible, this example is included too.

Run digit.py in an IDE to test it. Each DigitCollection is an object, for example:
>>> Digit("15", base=DECIMAL)
""")

    working.clear()
    digits = []
    polarity = 0
    base = wrap_point = DECIMAL

    request_input = True
    while request_input:
        working_value = input("digit values (comma separated): ")
        working_polarity = input("is positive: ")
        working_base = input("base (name ie. decimal): ")

        try:
            digits = list(map(int, working_value.split(",")))
            polarity = 1 if "n" in working_polarity.lower() else 0
            base, wrap_point = valid_base(working_base)
            request_input = False

        except ValueError as e:
            print(f"Invalid values entered.\n{e}")

    example = DigitCollection(digits, polarity, base, wrap_point)
    print(f'Str value  {example}')
    print(f'Numerals   {example.numeral()}')
    print(f'Int value  {example.value()}')
