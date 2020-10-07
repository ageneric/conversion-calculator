"""This numeric-style class includes DigitCollection,
see comment below / WIP.

(previously number.py)
"""

from constants import extended_numerals, BINARY, OCTAL, DECIMAL, HEXADECIMAL


def t_DigitCollection(value: int, base=10, base_mantissa=None):
    """Placeholder function to generate a DigitCollection of the
    specified base from a Python integer, using repeated division."""
    polarity_bit = 0 if value >= 0 else 1
    base_mantissa = base if base_mantissa is None else base_mantissa
    digits = []

    while value > 0:
        digits.insert(0, value % base)  # Remainder digits in reverse order.
        value = value // base_mantissa

    return DigitCollection(digits, polarity_bit, base, base_mantissa)


class DigitCollection:
    """Wraps an array of integer digits representing a number in any base."""

    def __init__(self, digits, polarity_bit=0, base=10, displayed_base=None):
        self.polarity = polarity_bit
        self.base = base
        self.base_mantissa = base if displayed_base is None \
            else displayed_base

        digits = tuple(map(int, list(digits)))  # Cast the digits iterable to tuple(int).
        if any(map(lambda n: n >= self.base, digits)):  # If any digits exceed the base number.
            raise ValueError(f"Digits {digits} cannot be represented in base {base}.")
        self.digits = digits

    def __repr__(self):
        return f'DigitCollection({self.digits}, ... {self.base})'

    def __str__(self):
        return f'{self.numeral()}: base {self.base}'

    def __add__(self, other):
        # TODO: Implement custom addition function.
        # Currently returns a new DigitCollection with the first number's base.
        return t_DigitCollection(self.value() + other.value(), self.base)

    # ----
    def value(self) -> int:
        """Returns the integer value of the represented number."""
        total = 0
        place_exponent = 0
        reversed_digits = reversed(self.digits)  # self.digits[::-1]

        for digit in reversed_digits:
            total += digit * self.base**place_exponent
            place_exponent += 1

        if self.polarity:
            total = -total

        return total

        # TODO: Implement custom conversion function.
    def convert(self, base, displayed_base=None):
        """Implements repeated division to build and return
        a DigitCollection of the specified base."""
        digits = []
        value = self.value()

        while value > 0:
            digits.insert(0, value % base)  # Remainder digits in reverse order.
            value = value // base

        return DigitCollection(digits, self.polarity, base)


    def numeral(self) -> str:
        """Returns the number as a single string, printed
        as individual digits in its numeric base."""
        numerals = []
        
        for digit in self.digits:
            if digit < 10:
                numerals.append(str(digit))
            else:
                numerals.append(extended_numerals[digit])

        return ''.join(numerals)


if __name__ == "__main__":
    x = DigitCollection((1,0,10), base=HEXADECIMAL)
    assert x.value() == 266
    assert (x + x).value() == x.value() * 2

    y = DigitCollection((2,4), base=OCTAL)
    assert y.value() == 20
    assert (x + y).value() == x.value() + y.value()

    z = DigitCollection("266").convert(BINARY)
    assert '100001010' in str(z)
    assert x.value() == z.value()
    assert y.value() == DigitCollection((2,0)).convert(OCTAL).value()

    print('DigitCollection: Test passed.')
