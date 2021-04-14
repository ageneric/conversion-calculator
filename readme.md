# Conversion Calculator
Made with Flask and Python 3.7 or 3.8

You may be able to try the [web app](https://generic.eu.pythonanywhere.com/) here, if it's running.

## Specification
Design and program a calculator which allows the user to, 

1. Convert between Denary, Binary and Hexadecimal.
2. The user can either choose to represent the negative binary number as either sign and magnitude or two's complement.
3. Allow the answer to be displayed in one's complement.
4. Convert between, Denary, Binary, Hexadecimal, Octal and BCD.
5. Show Denary, Binary and Hexadecimal addition and subtraction.
6. Interact with the program using a graphical user interface - in particular, this project will utilise Flask.
7. Print out the maths for each conversion in a suitable format for the user to understand the calculation.

## Data

This program defines `DigitValue` to represent an array of integer digits, providing conversion methods
to different bases and numeric systems.

Negative numeric values are specified with the polarity property (1 for negative, 0 for positive).
This is equivalent to the "sign bit" of a sign-and-magnitude binary number. -0 is invalid.

Binary coded decimal is represented using `base=DECIMAL, wrap_point=HEXADECIMAL` (not `BINARY`).
Use the `.pad_to_bytes()` method to return the number as binary.

## Program Use

May be run as a text-based demo by running main.py, or by running digit.py in an interactive Python console (i.e. the IDLE shell).
There is a Flask web app included. Use Flask with environment variable `FLASK_APP` set to `run_app.py`.
Example use of the `DigitValue` class and associated functionality can be found in digit.py under test().

Note: the intention of this project is to demonstrate computational methods for conversion,
rather than being a general-purpose and efficient library. However, digit.py is technically usable
as its own module for dealing with base conversions (optionally with working.py to enable working).

Provided "as is": no guarantee that this won't crash or break. The software, assets and associated files may be used, copied, modified and distributed without restriction.