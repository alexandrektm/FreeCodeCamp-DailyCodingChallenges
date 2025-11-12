# SpOoKy~CaSe
# Given a string representing a variable name, convert it to "spooky case" using the following constraints:
# 
# Replace all underscores (_), and hyphens (-) with a tilde (~).
# Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.
# For example, given hello_world, return HeLlO~wOrLd.

def spookify(boo):

        new_string = []
        state = 0

        for character in boo:

                if character in ("-","_"):

                        new_string.append("~")
                        continue

                if state == 0:

                        new_string.append(character.upper())
                        state = 1

                else:

                        new_string.append(character.lower())
                        state = 0
                
        boo_word = "".join(new_string)

        return boo_word