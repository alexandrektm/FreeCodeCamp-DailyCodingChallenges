def cost_to_fill(tankSize, fuelLevel, pricePerGallon):
    
    leftFill=float(tankSize)-float(fuelLevel)
    cost=leftFill*pricePerGallon
    
    result=f"${cost:.2f}"
    return result
    
print(cost_to_fill(15,9.5,3.98))