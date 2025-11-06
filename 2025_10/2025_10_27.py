# Integer Sequence
# Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.
# 
# For example, given 5, return "12345".

def sequence(n):

        listing = list(range(n+1))[1::]
        new_list = []
        for element in listing:
                new_list.append(f"{element}")
        final_list = "".join(new_list)

        return final_list

print(sequence(27))


# BETTER SOLUTION WITH COMPREHENSION:

def sequence(n):

        new_list = [str(i) for i in range(1, n + 1)]
        final_list = "".join(new_list)

        return final_list

print(sequence(27))