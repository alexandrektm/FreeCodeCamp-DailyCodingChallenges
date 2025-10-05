def generateSlug(string):
    
    skip = False
    result = []
    i = 0
    o = 0
    block = 0
    
    for char in string:
        i += 1
        char = char.lower()
        
        if char not in "qwertyuiopasdfghjklzxcvbnm 1234567890":
            result = result
            
        elif char == " ":
             
             if i == 1:
                 o=i
                 while list(string)[o-1] == " ":
                     o += 1
                     if o+1 > (len(string)-1):
                         result=result
                         skip = True
                         break
                     block += 1
             
             elif (i+1) > (len(string)-1):
                 result=result
                 
             elif block >= 1:
                 result=result
                 block -= 1
                 
             else:
                 o=i
                 while list(string)[o-1] == " ":
                     o += 1
                     if o+1 > (len(string)-1):
                         result=result
                         skip = True
                         break
                     block += 1
                     
                 if skip == False:
                     result.append("%20")
             
        else:
             result.append(char)
             
    result="".join(result)
    return result

print(generateSlug("  ?H^3-1*1]0!  W[0%R#1]D  "))




def generateSlug(string):
    
    skip = False
    result = []
    i = 0
    o = 0
    block = 0
    
    for char in string:

        char = char.lower()
        
        if char not in "qwertyuiopasdfghjklzxcvbnm 1234567890":
            result = result
            
        elif char == " ":

            if i == 0:
               result=result
            elif string[i-1] == " ":
               result=result
            else:
               result.append("%20")
             
        else:
            result.append(char)
            
        i += 1
    
             
    if result[len(result)-1] == "%20": 
       del result[len(result)-1]                          
    result="".join(result)
    return result

print(generateSlug("  ?H^3-1*1]0!  W[0%R#1]D  "))
