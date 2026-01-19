# Array Swap
# Given an array with two values, return an array with the values swapped.
# 
# For example, given ["A", "B"] return ["B", "A"].

def array_swap(arr):

    arr.append(arr.pop(0))

    return arr

print(array_swap([1,2]))