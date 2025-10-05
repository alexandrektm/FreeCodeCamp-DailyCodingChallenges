import os

def find_missing_numbers(arr):

    big = 0
    result = []

    for elem in arr:

        if elem > big:
            big = elem

    for i in range(big):

        if i == 0:
            result=result
        elif i not in arr:
            result.append(i)
        
    return result

os.system("cls")
print(find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]))