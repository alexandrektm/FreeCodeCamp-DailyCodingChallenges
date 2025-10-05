def digits_or_letters(s):
    
    dig = 0
    lett = 0
    result = ""
    
    for char in s:
        if char in "1234567890":
            dig += 1
        elif char.upper() in "QWERTYUIOPASDFGHJKLZXCVBNM":
            lett += 1
        else:
            result = result
       
        
    if dig > lett:
        result = "digits"
    elif lett > dig:
        result = "letters"
    else:
        result = "tie"
    
    return result
    
print(digits_or_letters("P455W0RD"))