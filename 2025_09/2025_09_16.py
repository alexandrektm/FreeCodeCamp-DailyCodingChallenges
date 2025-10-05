def capitalize(paragraph):

    capital = True
    temp = []

    for char in paragraph:
        if char == "." or char == "!" or char == "?":
            capital = True
            temp.append(char)
        elif char == " ":
            temp.append(char)
        elif capital:
            temp.append(char.upper())
            capital = False
        else:
            temp.append(char)

    result = "".join(temp)
    return result

print(capitalize("there's a space before this period . why is there a space before that period ?"))