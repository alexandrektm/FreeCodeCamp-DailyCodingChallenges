def is_mirror(a, b):

    la = []
    lb = []

    for char in a:
        if char.isalnum():
            la.append(char)
        else:
            la = la

    for char in b:
        if char.isalnum():
            lb.insert(0, char)
        else:
            lb = lb

    if la == lb:
        result = True
    else:
        result = False

    return result

print(is_mirror("Hello World","!dlroW !olleH"))