# Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.
# 
# Hexadecimal is a number system that uses 16 digits:
# 
# 0-9 represent values 0 through 9.
# A-F represent values 10 through 15.


def hex_to_decimal(hex):

    hex_values = {
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
    }

    decimal : int = 0
    multiplier : int = 1
    reversed_hex = list(hex)[::-1]

    for character in reversed_hex:

        decimal += hex_values[character] * multiplier
        multiplier *= 16

    return decimal

print(hex_to_decimal("A3F"))