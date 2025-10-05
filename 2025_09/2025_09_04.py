def repeat_vowels(s):

    ns = []
    o=0
    for char in s:
        if char in "AEIOUaeiou":

            if char in "Aa":
                ns.append(char)
                for i in range(o):
                    ns.append("a")
                o += 1
            if char in "Ee":
                ns.append(char)
                for i in range(o):
                    ns.append("e")
                o += 1
            if char in "Ii":
                ns.append(char)
                for i in range(o):
                    ns.append("i")
                o += 1
            if char in "Oo":
                ns.append(char)
                for i in range(o):
                    ns.append("o")
                o += 1
            if char in "Uu":
                ns.append(char)
                for i in range(o):
                    ns.append("u")
                o += 1

        else:
            ns.append(char)

    result="".join(ns)

    return result

print(repeat_vowels("I like eating ice cream in Iceland"))