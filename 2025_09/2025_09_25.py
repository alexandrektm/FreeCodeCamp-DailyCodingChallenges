def second_largest(arr):

    temp = [0,0]

    for el in arr:

        if el > temp[0]:
            temp.insert(0,el)
            temp.pop(2)

        elif el > temp[1]:
            temp.pop(1)
            temp.append(el)

        else:
            temp = temp

        print(temp)

    result =  temp[1]

    return result

print(second_largest([2, 3, 4, 6, 6]))