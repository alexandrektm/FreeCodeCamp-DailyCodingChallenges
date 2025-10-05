def rgb_to_hex(rgb):
    
    listing=[]
    red_list=[]
    green_list=[]
    blue_list=[]
    for i in rgb:
        listing.append(i)
        
    for i in range(4):
        listing.pop(0)
     
    
    r=1      
    for red_elem in listing:
        if red_elem == ",":
            break
        else:
            red_list.append(red_elem)
            r+=1
    del listing[:r]       
    

    g=1      
    for green_elem in listing:
        if green_elem == ",":
            break
        else:
            green_list.append(green_elem)
            g+=1
    del listing[:g]       
            
            
    b=1      
    for blue_elem in listing:
        
        if blue_elem == ")":
            break
        else:
            blue_list.append(blue_elem)
            b+=1
            
    del listing[:b]
    
    final_list=[red_list, green_list, blue_list] 
    
    result=""
    for lista in final_list:
        
        end=""
        for num in lista:
            
            end=end+num
            
        num=int(end)
        hex1=num//16
        hex2=num%16
        hexa_pool=[
        "0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"
         ]
        hex1=hexa_pool[hex1]
        hex2=hexa_pool[hex2]
        
        result=result+hex1+hex2
        
    result="#"+result
    return result

print(rgb_to_hex("rgb(255, 255, 255)"))