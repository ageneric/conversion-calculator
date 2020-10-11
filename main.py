"""A program which manually converts between
bases and number representation systems.

Task 1.4.1.f Kevin Gao
"""

from constants import *
from digit import DigitCollection

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


if __name__ == '__main__':
    print("  * Work in progress: user interface is not currently proofed.\n")

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

    print('\n  * New number from integer value.\n')
    value = 0
    request_input = True
    while request_input:
        working_value = input("base 10 value: ")
        working_base = input("base (name ie. decimal): ")

        try:
            value = int(working_value)
            base, wrap_point = valid_base(working_base)
            request_input = False
        except ValueError as e:
            print(f"Invalid values entered:\n{e}")

    example = DigitCollection.init_from_value(value, base, wrap_point)
    print(f'Str value  {example}')
    print(f'Numerals   {example.numeral()}')
    print(f'Int value  {example.value()}')
