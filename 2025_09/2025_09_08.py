def build_acronym(s):

    slist=s.split(" ")
    final=[]
    
    for word in slist:
        
        not_list = ["a", "for", "an", "and", "by", "of" ]
        
        if word not in not_list:
        
            wlist=list(word)
            acro=wlist[0].upper()
            final.append(acro)
    
        else: 
    
            final=final

    final = "".join(final)

    return final