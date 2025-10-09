#   Space Week Day 6: Moon Phase
#   For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

#   Use a simplified lunar cycle of 28 days, divided into four equal phases:

#   "New": days 1 - 7
#   "Waxing": days 8 - 14
#   "Full": days 15 - 21
#   "Waning": days 22 - 28
#    After day 28, the cycle repeats with day 1, a new moon.

# Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
# You will not be given any dates before the reference date.
# Return the correct phase as a string.



def moon_phase(date_string):

    day_counter: int = -5

    temporary_list = date_string.strip("").split("-")
    year, month, day = int(temporary_list[0]), int(temporary_list[1]), int(temporary_list[2])

    # PARSING YEAR

    day_counter += (year-2000) * 365
    day_counter += (year-2000) // 4
    day_counter -= (year-2000) // 100
    day_counter += (year-2000) // 400

    # PARSING MONTH

    month_dictionary = {

        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,

    }

    if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
        month_dictionary[2] = 29
    
    for iteration in range(1,month):
        day_counter += month_dictionary[iteration]

    # PARSING DAYS

    day_counter += day

    # CALCULATING

    day_counter = day_counter % 28

    if 1 <= day_counter <= 7:
        return "New"
    
    elif 8 <= day_counter <= 14:
        return "Waxing"
    
    elif 15 <= day_counter <= 21:
        return "Full"
    
    elif (22 <= day_counter <= 28) or (day_counter == 0):
        return "Waning"

    
print(moon_phase("2000-01-13"))