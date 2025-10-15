# 24 to 12
# Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".
# 
# The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

def to_12(raw_time):

    hours = int(raw_time[0:2])
    minutes = raw_time[2:4]
    type = "AM"

    if (hours == 0):
        hours = 12

    elif (hours >= 12):
        type = "PM"
        if (hours > 12):
            hours = hours % 12

    return f"{hours}:{minutes} {type}"

print(to_12("0900"))