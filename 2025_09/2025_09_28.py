def get_headings(s):
    
    temp = s.split(",")
    result : list = []
    
    for el in temp:
        el = el.strip()
        result.append(el)

    return result
    
print(get_headings("username, email , signup date "))