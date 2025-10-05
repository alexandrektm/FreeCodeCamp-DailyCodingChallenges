def speeding(cars,limit):
    
    temp=[]
    
    for car in cars:
        if car > limit:
            temp.append(car)
            
    num=len(temp)
    if num > 0:
        avr = (sum(temp)/len(temp))-limit
    else:
        avr = 0
    
    result = [num,avr]
    
    return result
    
print(speeding([40,45,44,50,112,39],55))