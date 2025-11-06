# Duration Formatter
# Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:
# 
# Seconds: Should always be two digits.
# Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
# Hours: Should be included only if they're greater than zero.

def format(general_seconds):

        final_seconds:int = general_seconds % 60
        general_minutes:int = general_seconds // 60
        final_minutes:int = general_minutes % 60
        hours:int = general_minutes // 60


        if final_minutes < 10 and hours > 0:

                final_minutes = "0" + str(final_minutes)

        if final_seconds < 10:

                final_seconds = "0" + str(final_seconds)


        if hours > 0:

                time = f"{hours}:{final_minutes}:{final_seconds}"
                return time

        else:

                time = f"{final_minutes}:{final_seconds}"
                return time


print(format(1))