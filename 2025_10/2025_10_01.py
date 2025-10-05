def to_decimal(bin):

    result : int = 0
    mult : int = 1
    bin = bin[::-1]

    for dig in bin:

        if dig == "1":
            result += mult
        
        mult *= 2

    return result


print(to_decimal("1010"))