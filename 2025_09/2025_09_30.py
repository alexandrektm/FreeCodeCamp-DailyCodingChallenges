def format_number(number):

    count : int = 1
    final : list = ["+"]

    for dig in number:

        if count == 1:
            final.append(dig)
            final.append(" ")
            final.append("(")
        
        elif count == 4:
            final.append(dig)
            final.append(")")
            final.append(" ")

        elif count == 7:
            final.append(dig)
            final.append("-")

        else:
            final.append(dig)

        count += 1

    number = "".join(final)

    return number

print(format_number("15554354792"))