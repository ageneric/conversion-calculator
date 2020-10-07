"""A program to convert between bases and number
representation systems.

Task 1.4.1f Kevin Gao
"""

from constants import *
from digit import DigitCollection, t_DigitCollection


def valid_base(user_input: str):
    lowercase_input = user_input.lower()
    
    if lowercase_input in name_binary:
        return 2
    elif lowercase_input in name_octal:
        return 8
    elif lowercase_input in name_decimal:
        return 10
    elif lowercase_input in name_hexadecimal:
        return 16
    
    raise ValueError('Invalid base: base not found. Accepted bases include \
binary, octal, decimal and hexadecimal.')


if __name__ == '__main__':
    print("  * Work in progress: user interface is not currently proofed.\n")

    digits = []
    base = DECIMAL
    request_input = True
    while request_input:
        working_value = input("digit values (comma separated, lower than base): ")
        working_base = input("base (name ie. decimal): ")

        try:
            digits = list(map(int, working_value.split(",")))
            base = valid_base(working_base)
            break
        except ValueError:
            print("Invalid values entered.")

    example = DigitCollection(digits, base)
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
            base = valid_base(working_base)
            break
        except ValueError:
            print("Invalid values entered.")

    example = t_DigitCollection(value, base)
    print(f'Str value  {example}')
    print(f'Numerals   {example.numeral()}')
    print(f'Int value  {example.value()}')
