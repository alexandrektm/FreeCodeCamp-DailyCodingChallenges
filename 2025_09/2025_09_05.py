def is_valid_ipv4(ipv4):

    skip = False
    result = False

    iplist=ipv4.split(".")
    if len(iplist) != 4:
        result = False
        skip = True

    if not skip:

        for item in iplist:
            if item == "" or item == " ":
                result = False
                break
                
            if item.isdigit():

                if (len(list(item)) >= 2 and int(list(item)[0]) == 0):
                    result = False
                    break

                else:
                    check = int(item)
                    if 0 <= check <= 255:
                        result = True
                    else:
                        result = False
                        break

            else:
                result = False
                break
            
    return result

print(is_valid_ipv4("255.01.50.111"))