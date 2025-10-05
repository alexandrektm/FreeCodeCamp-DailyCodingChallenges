def all_unique(s):

    final=True
    temp_list=[]
    for char in s:
        
        if char in temp_list:
            final=False
            break
        
        temp_list.append(char)
            

    return final
    
print(all_unique("ag4tf766"))