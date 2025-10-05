def to_binary(decimal):

    binary : str = ""

    while decimal > 0:

        remainder = decimal % 2
        decimal = decimal // 2

        binary = str(remainder) + binary

    return binary

print(to_binary(99))