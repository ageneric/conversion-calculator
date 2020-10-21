extended_numerals = {
    10: 'a', 11: 'b', 12: 'c', 13: 'd',
    14: 'e', 15: 'f'
}

inv_extended_numerals = {
    value: key for key, value in extended_numerals.items()
}

BREAK_ON_ERROR = True
SAVE_WORKING = True
log_directory = 'data/working.log'

name_binary = ('2', 'bin', 'binary')
name_octal = ('8', 'oct', 'octal')
name_decimal = ('10', 'dec', 'decimal', 'denary')
name_hexadecimal = ('16', 'hex', 'hexadecimal')
name_bcd = ('bcd', 'binary coded decimal', 'packed')

BINARY = 2
OCTAL = 8
DECIMAL = 10
HEXADECIMAL = 16
