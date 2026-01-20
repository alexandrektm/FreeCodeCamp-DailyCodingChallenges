
def to_consonant_case(s):

    new_s = []
    for char in s:
        if char == "-":
            new_s.append("_")
        elif char in "aeiouAEIOU":
            new_s.append(char.lower())
        else:
            new_s.append(char.upper())

    s = "".join(new_s)

    return s