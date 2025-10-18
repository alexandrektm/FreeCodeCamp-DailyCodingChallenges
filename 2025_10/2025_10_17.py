# Credit Card Masker
# Given a string of credit card numbers, return a masked version of it using the following constraints:
# 
# The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
# Replace all numbers, except the last four, with an asterisk (*).
# Leave the remaining characters unchanged.
# For example, given "4012-8888-8888-1881" return "****-****-****-1881".

def mask(card):

    if "-" in card:
        masked_card = "****-****-****-"+card[15:19]
    else:
        masked_card = "**** **** **** "+card[15:19]

    masked_card = "".join(masked_card)

    return masked_card

print(mask("2223 0000 4845 0010"))