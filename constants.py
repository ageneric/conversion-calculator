extended_numerals = {
    10: 'a', 11: 'b', 12: 'c', 13: 'd',
    14: 'e', 15: 'f'
}

inv_extended_numerals = {
    value: key for key, value in extended_numerals.items()
}

name_binary = ('bin', 'binary')
name_octal = ('oct', 'octal')
name_decimal = ('dec', 'decimal', 'denary')
name_hexadecimal = ('hex', 'hexadecimal')
name_bcd = ('bcd', 'binary coded decimal', 'packed')

BINARY = 2
OCTAL = 8
DECIMAL = 10
HEXADECIMAL = 16
