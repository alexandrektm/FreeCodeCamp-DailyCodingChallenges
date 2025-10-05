def number_of_photos(mb,gb):
    
    gb = gb*1000
    result = int(gb//mb)
    return result
    
 
print(number_of_photos(3.5,5.5))