def adjust_thermostat(temp, target):

    if temp > target:
        result = "cool"
    elif temp == target:
        result = "hold"
    else:
        result = "heat"

    return result