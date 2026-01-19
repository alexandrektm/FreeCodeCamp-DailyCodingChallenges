# Free Shipping
# Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.
# 
# The given array will contain items from the list below:
# 
# Item	Price
# "shirt"	34.25
# "jeans"	48.50
# "shoes"	75.00
# "hat"	19.95
# "socks"	15.00
# "jacket"	109.95
# 


def gets_free_shipping(cart, minimum):

    item_prices = {
        "shirt": 34.25,
        "jeans": 48.00,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95
    }

    item_total:int = 0

    for item in cart:
        item_total += item_prices[item]

    if item_total >= minimum:
        return True
    return False