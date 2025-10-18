def is_spam(number):

    result : bool = False
    count, part, rep = 0, 0, 1
    r : None = None
    p2 : str = ""
    p3 : int = 0

    for n in number:


        if not n.isdigit():
            continue
        n = int(n)
            

        if n == r:
            rep += 1
        else:
            rep = 1
            r = n
        if rep >= 4:
            return True


        if part == 0 and count == 0 and n != 0:           
            return True
        elif part == 0:
            part += 1
    

        if part == 1 and count > 2:             
            return True     
        elif part == 1 and n == " ":
            part += 1
            continue
        elif part == 1:
            count += 1
            continue
            

        if (part == 2) and not (n == " "):     
            p2 : str = p2 + str(n)
            continue
        elif part == 2:
            if int(p2) > 900 or int(p2) < 200:
                return True
            else:
                part += 1
                continue


        if part == 3 and n == "-":                       
            part += 1
            continue
        elif part == 3:
            p3 += n
            continue


        if part == 4 and p3 == n:
            return True

    return result

print(is_spam("+0 (555) 564-1987"))