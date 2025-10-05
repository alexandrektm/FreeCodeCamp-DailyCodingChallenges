def parse_roman_numeral(numeral):

    number=0
    dict= {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        }
    temp_list=list(numeral)
    i=0
    temp_value=0
    
    
    while i <= len(temp_list)-1:
        
        if i < len(temp_list)-1:
            if dict[temp_list[i]] < dict[temp_list[i+1]]:
                
                temp_value=dict[temp_list[i+1]]-dict[temp_list[i]]
                i += 1
                
                
            else:
                
                temp_value=dict[temp_list[i]]
                
            
        else:
            
            temp_value=dict[temp_list[i]]
            
            
        i += 1
        number=number+temp_value
        
        
    return number
    
    
print(parse_roman_numeral("XCIX"))