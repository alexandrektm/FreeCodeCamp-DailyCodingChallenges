import os

def too_much_screen_time(hours):

    result = False
    skip = False

    for day in hours:
        if day >= 10:
            result = True
            skip = True
            break
        
    if skip != True:
        o = 2
        for i in range(len(hours)-2):
            aver3 = (hours[o]+hours[o-1]+hours[o-2])/3
           # print(f"This is hours o: {hours[o]}")
           # print(f"This is hours o-2: {hours[o-2]}")
           # print(f"This is aver3: {aver3}")
            if aver3 >= 8:
                result = True
                skip = True
                break
            o += 1

    if skip != True:
        aver7 = sum(hours)/7
        if aver7 >= 6:
            result = True

    return result

os.system("cls")
print(too_much_screen_time([3, 9, 4, 8, 5, 7, 6]))
