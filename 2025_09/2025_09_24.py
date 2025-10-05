def is_perfect_square(n):

    if n >= 0:

        if (n ** 0.5) % 1 == 0:
            result = True
        else:
            result = False

    else:

        result = False

        
    return result

print(is_perfect_square(9))