# Conversion Calculator
(Assignment) for Python 3.7 or 3.8

You may be able to try the [web app](https://generic.eu.pythonanywhere.com/) here, if it's running.

## Specification
Design and program a calculator which allows the user to, 

1. 1. Convert from a binary number to a denary number 
   2. Convert from a denary number to a binary number 
   3. Convert from a negative denary number to a negative binary number 
   4. Convert from a negative binary number to a negative denary number 

2. Convert between Denary, Binary and Hexadecimal. 
3. The user can either choose to represent the negative binary number as either sign magnitude or two's complement. 
4. Allow the answer to be displayed in one's complement. 
5. Convert between, Denary, Binary, Hexadecimal, Octal and BCD. 
6. Modify so values can be added and subtracted in your program. Show Denary, Binary and Hexadecimal addition and subtraction. 
7. Interact with the program using a graphical user interface - in particular, this project will utilise Flask. 
8. Print out the maths for each conversion in a suitable format for the user to understand the calculation. 

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

Provided "as is": no guarantee that this won't crash or break. The software and associated documentation files
may be used, copied, modified and distributed without restriction, as long as this isn't your assignment work :)