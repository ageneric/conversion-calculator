# Conversion Calculator
Task 1.4.1.f - CPython 3.7 or 3.8

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

This program defines DigitCollection(), wrapping an array of integer digits and providing conversion methods.

Negative numeric values are specified with the polarity property (1 for negative, 0 for positive).
This is equivalent to the "sign bit" of a sign-and-magnitude binary number.

Binary coded decimal is represented using `base=DECIMAL, wrap_point=HEXADECIMAL` (not `BINARY`).
Use the `.pad_to_bytes()` method to return the number as binary.

Perform addition for place-value numbers using `DigitCollection() + DigitCollection() -> DigitCollection()`.

## Program Use

The program can be run in a limited, text-based mode by running main.py.
There is also a Flask web app included. Use Flask with FLASK_APP = run_app.py. The calculation is not yet returned.

Alternatively, running digit.py in an interactive Python console (ie. the IDLE shell) will give access to all core functionality.
