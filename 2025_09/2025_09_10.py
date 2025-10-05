def array_diff(arr1, arr2):

    arr1and2=[]
    arr3=arr1+arr2

    for elem in arr1:
        if elem in arr2:
            arr1and2.append(elem)
        
    for elem in arr1and2:
        if elem in arr3:
            arr3.remove(elem)
            arr3.remove(elem)
        
    arr3.sort()

    return arr3
