# Tip Calculator
# Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.
# 
# Prices will be given in the format: "$N.NN".
# Custom tip percents will be given in this format: "25%".
# Return amounts in the same "$N.NN" format, rounded to two decimal places.
# For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].


def calculate_tips(meal_price, custom_tip):

    formatted_price = float(meal_price[1:])
    formatted_tip = float(custom_tip[:(len(custom_tip)-1)])/100

    tip_15 = formatted_price * 0.15
    tip_20 = formatted_price * 0.20
    tip_custom = formatted_price * formatted_tip

    tip_prices = [f"${tip_15:.2f}", f"${tip_20:.2f}", f"${tip_custom:.2f}"]

    return tip_prices

print(calculate_tips("$10.00", "25%"))