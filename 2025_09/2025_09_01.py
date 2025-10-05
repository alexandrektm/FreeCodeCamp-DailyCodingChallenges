def tribonacci_sequence(start_sequence, length):        
    
    result=[]

    while len(start_sequence) < 3:
        start_sequence.insert(0,0)
    
    if length <= 3:
        for i in range(length):
            result.append(start_sequence[i])

    else:
        for i in range(length-3):
            last_three=start_sequence[-3:]
            start_sequence.append(sum(last_three))
        
        result=start_sequence

    return result

    
print (tribonacci_sequence([21, 32, 43], 5))