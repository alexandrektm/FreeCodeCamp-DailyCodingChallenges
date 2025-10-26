# Hidden Treasure
# Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:
# 
# The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.
# 
# Each cell in the 2D array will contain one of the following values:
# 
# "-": No treasure.
# "O": A part of the treasure that has not been found.
# "X": A part of the treasure that has already been found.
# If the dive location has no treasure, return "Empty".
# 
# If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".
# 
# If the dive location finds the last unfound part of the treasure, return "Recovered".


def dive(map, coordinates):

    row = coordinates[0]
    column = coordinates[1]

    if map[row][column] == "-":
        return "Empty"
    
    if map[row][column] == "X":
        return "Found"
    
    if map[row][column] == "O":
        return "Recovered"

    return map

print(dive([[ "-", "X"], 
            [ "-", "X"], 
            [ "-", "O"]], [2, 1]))