# String Count
# Given two strings, determine how many times the second string appears in the first.
# 
# The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.

def count(text, parameter):

    if parameter not in text:
        return 0

    check_length = len(parameter)
    i = 0
    counting : int = 0

    while (check_length+i) <= len(text):

        if parameter == text[i:(check_length+i)]:
            counting += 1
        
        i += 1

    return counting

print(count("ababab","ab"))