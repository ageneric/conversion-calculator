extended_numerals = {
    10: 'a', 11: 'b', 12: 'c', 13: 'd',
    14: 'e', 15: 'f'
}

inv_extended_numerals = {
    value: key for key, value in extended_numerals.items()
}

BREAK_ON_ERROR = True
USE_WORKING = True  # Record the methods taken by the program.
LOG_WORKING = False  # Write the working log to a file & print to console.
log_directory = 'data/working.log'

name_binary = ('2', 'bin', 'binary')
name_octal = ('8', 'oct', 'octal')
name_decimal = ('10', 'dec', 'decimal', 'denary')
name_hexadecimal = ('16', 'hex', 'hexadecimal')
name_bcd = ('bcd', 'binary coded decimal', 'packed')

conversions = ('2', '8', '10', '16', 'bcd')
functions = ('add', 'numerals', 'value', 'pad_to_bytes',
             'one_complement', 'two_complement', 'sign_and_magnitude')

CONVERSION = 0
FUNCTION = 1
NEW_NUMBER = 2

BINARY = 2
OCTAL = 8
DECIMAL = 10
HEXADECIMAL = 16
