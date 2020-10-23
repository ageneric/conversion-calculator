"""This numeric-style class represents an integer value in a specified base.
It it stored digit-wise as a demonstration of computing addition and
other numeric methods. Note: an "array" here refers to either Tuple or List.

Please see test() for example usage. Run this file to run all tests.

Digit.py may be used as a module/package (if you really want to).
This requires constants.py, and also working.py if working is enabled.
(Kevin Gao) https://github.com/ageneric/conversion-calculator/
"""

# Module imports --
try:
    from constants import *
except ModuleNotFoundError:
    raise ModuleNotFoundError("Digit: Requires constants.py.")

try:
    from working import log_method
except ModuleNotFoundError:
    if USE_WORKING:
        raise ModuleNotFoundError("Digit: If USE_WORKING (constants.py) is enabled, \
requires working.py, in order to record working. Please either disable USE_WORKING, \
in constants.py, or add the required file.")
    else:
        def log_method(*placeholder):
            pass

# Definitions --
def pad_left(content: iter, padding_length: int, fillchar=0):
    """Pads zeroes to the start of the content iterable."""
    final = [fillchar] * padding_length
    final.extend(content)
    return final

def flip_values(digits: iter, max_value: int):
    complement = []
    for digit in digits:
        complement.append(max_value - digit)
    return complement

def sanitise_digits(digits: iter, base: int, wrap_point: int):
    # Converts to a list of integer values.
    digits = list(map(int, digits))

    # Raise an error if any digits exceed the base.
    if any(map(lambda n: n >= wrap_point, digits)):
        raise ValueError(f'digits {digits} cannot be represented in a base ({base}) \
system where numbers wrap at {wrap_point}.')
    return digits

def two_complement_value(digits: iter, base=2):
    total = 0
    place_exponent = 0
    complement_bit, *normal_bits = digits

    # Add each digit's place value, least digit first. self.digits[::-1]
    for bit in reversed(normal_bits):
        total += bit * base ** place_exponent
        place_exponent += 1
    # Add the most significant, negative value bit.
    total += complement_bit * -1 * base ** place_exponent

    return total


class DigitList:
    """Wraps a list of integer digits, with a specified
    base. Provides methods to represent this number.
    Does not assume a place-value."""

    def __init__(self, digits, base=10, wrap_point=None):
        self.base = base
        # wrap_point: the digit wrap-around point used:
        # packed binary coded decimal / BCD would use (base=10, wrap_point=16).
        self.wrap_point = base if wrap_point is None else wrap_point

        self.digits = sanitise_digits(digits, self.base, self.wrap_point)

    def __repr__(self):
        return f'DigitList({self.digits}, {self.base}, {self.wrap_point})'

    def __str__(self):
        if self.base == self.wrap_point:
            return f'(#{self.numeral()}: base {self.base})'
        elif self.base == DECIMAL and self.wrap_point == HEXADECIMAL:
            return f'(#{self.numeral()}: BCD, base 10 / 16)'
        else:
            return f'(#{self.numeral()}: Custom, base {self.base} / {self.wrap_point})'

    @staticmethod
    def add_iterable(first_digits, second_digits, base):
        """Adds digits together within the base specified."""
        if len(first_digits) != len(second_digits):
            raise UserWarning("the digits to be added have not been padded to \
the same length. This may cause digits to be skipped during addition.")

        log_method('Pair digits together and add', first_digits, second_digits,
                   f'in base {base}', priority_level=1)
        result_digits = []

        # Iterate through pairs of digits, least digit first, and perform addition.
        carry = 0
        for first, second in zip(reversed(first_digits), reversed(second_digits)):
            _sum = first + second + carry
            log_method(f'Find sum of', first, second, carry, f'total {_sum}')
            if _sum >= base:
                carry, _sum = divmod(_sum, base)
                log_method(f'Total value has carry')
            else:
                carry = 0  # Reset carry so that values are only carried over once.
            result_digits.insert(0, _sum)

        log_method(f'Partial addition result', result_digits, f'with carry {carry}')
        return result_digits, carry

    # -- representation methods --
    def pad_to_bytes(self):
        """Pads digits (converted to binary) with zeroes such that
        bits are byte-aligned. Always returns an array of bits.
        Always pads at least one redundant zero, even if digits
        are already byte-aligned: (+/-)11111111 -> 0000000011111111."""
        log_method('Pad to byte-aligned binary', self, priority_level=0)
        positive_equivalent = DigitValue(self.digits, 0, self.base, self.wrap_point)
        binary = positive_equivalent.convert_base(BINARY)
        bits_needed = len(binary.digits)

        # Returns the binary digit array, consisting of [padding...] + [digits...]
        padding_length = 8 - (bits_needed % 8)
        bits = pad_left(binary.digits, padding_length)
        log_method('Padded binary', bits, f'with padding length {padding_length}')
        return bits

    def numeral(self):
        """Returns the number as a single string, represented
        as individual digits in its numeric base."""
        numerals = []

        for digit in self.digits:
            if digit < 10:
                numerals.append(str(digit))
            else:
                numerals.append(extended_numerals[digit])

        return ''.join(numerals)


class DigitValue(DigitList):
    """Wraps an array of integer digits representing a number in any base.
    Represents negative numbers with the polarity variable."""

    def __init__(self, digits, polarity_bit=0, base=10, wrap_point=None):
        if polarity_bit == 0 or polarity_bit == 1:
            self.polarity = polarity_bit
        else:
            # Invalid polarity bit provided (personally a common syntax error).
            if polarity_bit in [BINARY, OCTAL, DECIMAL, HEXADECIMAL]:
                error_message = f'polarity bit must be either 0 (positive) or \
1 (negative).\n  Did you mean DigitValue({digits}, base={polarity_bit}...)?'
            else:
                error_message = f'polarity bit must be either 0 (positive) or \
1 (negative), not {polarity_bit}.'
            raise ValueError(error_message)

        super().__init__(digits, base, wrap_point)

    @classmethod
    def init_from_value(cls, value: int, base=10, wrap_point=None):
        """Initialises a new DigitValue with the value of
        the integer specified. Accepts numeric-valid strings."""
        polarity_bit = 0 if int(value) >= 0 else 1
        wrap_point = base if wrap_point is None else wrap_point
        log_method('Initialise new custom number', value, f'in base {base}', wrap_point,
                   priority_level=0)

        digits = str(abs(int(value)))
        return cls(digits, polarity_bit).convert_base(base, wrap_point)

    def __repr__(self) -> str:
        return f'DigitValue({self.digits}, {self.polarity}, \
{self.base}, {self.wrap_point})'

    def __str__(self) -> str:
        if self.base == self.wrap_point:
            return f'({self.numeral()}: base {self.base})'
        elif self.base == DECIMAL and self.wrap_point == HEXADECIMAL:
            return f'({self.numeral()}: BCD, base 10 / 16)'
        else:
            return f'({self.numeral()}: Custom, base {self.base} / {self.wrap_point})'

    def __add__(self, other):
        """Add together two DigitValue instances. Positive
        numbers are added within the base of the left component.
        Negative numbers add using binary two's complement.
        Returns its answer in the base of the left component."""
        if not isinstance(other, self.__class__):
            raise TypeError('unsupported operand type(s) for +. Addition \
is only supported between two DigitValue() instances.')

        _self = self
        is_two_complement = [False, False]

        # Converts negative numbers to two's complement for cleaner addition.
        if self.polarity:
            log_method("First number is negative. Convert to two's complement")
            _self = self.two_complement()
            is_two_complement[0] = True

        if other.polarity:
            log_method("Second number is negative. Convert to two's complement")
            other = other.two_complement()
            is_two_complement[1] = True

        # After the first's base is set, convert the other component to the same base.
        log_method('Convert both numbers to the same base')
        if any(is_two_complement):
            if not is_two_complement[0]:  # Converts if not already a binary complement.
                _self = _self.convert_base(other.base, other.wrap_point)
            elif not is_two_complement[1]:
                other = other.convert_base(_self.base, _self.wrap_point)
        else:
            other = other.convert_base(self.base, self.wrap_point)
        first_digits = _self.digits
        second_digits = other.digits

        # Pad each to the same length, so that the place values match up for each digit.
        length_needed = max(len(first_digits), len(second_digits))

        first_digits = pad_left(first_digits, length_needed - len(first_digits),
                                fillchar=int(is_two_complement[0]))
        second_digits = pad_left(second_digits, length_needed - len(second_digits),
                                 fillchar=int(is_two_complement[1]))

        # Add the digits together; store the result as two's complement in result_digits.
        result_digits, carry = self.add_iterable(first_digits, second_digits, _self.base)

        if not any(is_two_complement):
            # For positive values the carry must also be checked,
            # since it holds the sum of the most significant bits.
            if carry:
                result_digits.insert(0, carry)
            # For positive two's complement, the first digit must stay a zero.
            if result_digits[0] != 0:
                result_digits.insert(0, 0)
            log_method('As the sum is positive, the carry is checked and added to the result.', result_digits)
        else:
            # If either component is negative the carry can be safely ignored.
            log_method('As one of the numbers is negative, the carry can be safely ignored')

        # Convert the final sum to its non-normalised value.
        result_value = two_complement_value(result_digits, _self.base)
        # Finally, switch back to the original base of the first component.
        result = DigitValue.init_from_value(result_value, self.base, self.wrap_point)
        log_method('As one of the numbers is negative, the carry can be safely ignored', priority_level=1)
        return result

    # -- numeric methods --
    def value(self) -> int:
        """Returns the integer value of the represented number."""
        total = 0
        place_exponent = 0

        # Add each digit's place value, least digit first. self.digits[::-1]
        for digit in reversed(self.digits):
            total += digit * self.wrap_point ** place_exponent
            place_exponent += 1

        if self.polarity:
            total = -total

        return total

    def convert_base(self, base: int, wrap_point=None):
        """Implements repeated division to convert to and
        return a DigitValue of the specified base."""
        wrap_point = base if wrap_point is None else wrap_point
        log_method('Base conversion', self, f'new base {base}', wrap_point, priority_level=1)

        if base == self.base and wrap_point == self.wrap_point:  # Optimisation check.
            return DigitValue(self.digits, self.polarity, base, wrap_point)

        digits = []
        value = abs(self.value())
        run_at_least_once = False

        log_method('Use repeated division to find each place-value digit in the new base.')
        while value > 0 or not run_at_least_once:
            value, new_digit = divmod(value, base)
            digits.insert(0, new_digit)  # Remainders are inserted in reverse order.

            if USE_WORKING:
                log_method('Value divided by the base', f'result {value}', f'remainder {new_digit}')
            run_at_least_once = True

        log_method('Base conversion result', digits)
        return DigitValue(digits, self.polarity, base, wrap_point)

    def negative(self):
        """Return a copy with the opposite polarity."""
        new_polarity = (self.polarity + 1) % 2  # Flip polarity (1 -> 0, 0 -> 1)
        return DigitValue(self.digits, new_polarity, self.base, self.wrap_point)

    # -- representation methods --
    def one_complement(self):
        """Return the one's complement of the number, as an
        array of byte-aligned binary. If the number is negative,
        this will flip all bits; ensures the first bit is 1."""
        log_method("One's complement", self, priority_level=1)
        padded_binary = self.pad_to_bytes()
        if self.polarity:
            return DigitList(flip_values(padded_binary, 1), BINARY)
        else:
            log_method("Value is positive: two's complement is equivalent to binary")
            return DigitList(padded_binary, BINARY)

    def two_complement(self):
        """Return the two's complement of the number."""
        log_method("Two's complement", self, priority_level=1)
        if self.polarity:
            _one_complement = self.one_complement()
            log_method("Use one's complement value in order to calculate two's complement",
                       _one_complement, priority_level=0)
            # Pad "1" with leading zeroes, so it can be added to the one's complement.
            log_method("Increment one's complement by 1")
            one = pad_left((1,), len(_one_complement.digits) - 1)
            incremented, _ = _one_complement.add_iterable(_one_complement.digits, one,
                                                          _one_complement.base)
            return DigitList(incremented, BINARY)
        else:
            log_method("Value is positive: two's complement is equivalent to binary")
            return DigitList(self.pad_to_bytes(), BINARY)

    def sign_and_magnitude(self):
        signed_binary = self.pad_to_bytes()
        if self.polarity:
            signed_binary[0] = 1

        return DigitList(signed_binary, BINARY)

    def numeral(self) -> str:
        """Returns the number represented as a single string
        of the given base, with a sign symbol to mark its polarity."""
        if self.polarity:
            return '-' + super().numeral()
        else:
            return super().numeral()


def test():
    x = DigitValue((1, 0, 10), base=HEXADECIMAL)
    assert x.value() == 266
    assert (x + x).value() == x.value() * 2

    y = DigitValue((2, 4), base=OCTAL)
    assert y.value() == 20

    additive = (x + y).value()
    assert additive == x.value() + y.value()
    assert additive == (y + x).value()

    z = DigitValue((2, 6, 6), 1, DECIMAL)
    assert z.convert_base(BINARY).digits == [1, 0, 0, 0, 0, 1, 0, 1, 0]
    assert (z + z).value() == z.value() * 2
    assert (x + z).value() == 0

    two_complement = x.negative().two_complement()
    assert -x.value() == two_complement_value(two_complement.digits) == x.negative().value()

    no_overflow = DigitValue((0, 1, 1, 1, 1, 1, 1, 1), base=BINARY)
    assert (no_overflow + no_overflow + no_overflow).value() == no_overflow.value() * 3

    _dec = DigitValue((2, 5), base=DECIMAL)
    _bcd = _dec.convert_base(DECIMAL, HEXADECIMAL)
    assert _bcd.digits == _dec.digits
    assert _bcd.pad_to_bytes() == [0, 0, 1, 0,  # "2"
                                   0, 1, 0, 1]  # "5"

    print("DigitValue: test passed.")


if __name__ == "__main__":
    test()
