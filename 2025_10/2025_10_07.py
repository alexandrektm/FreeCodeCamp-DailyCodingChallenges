def find_landing_spot(matrix):

    landing_spot = []
    danger_level : int = 0
    min_danger : int = 9999999

    for index_i, row in enumerate(matrix):
        for index_j, element in enumerate(row):
            if element != 0:
                continue

            if (index_i != 0):
                danger_level += matrix[index_i-1][index_j]

            if (index_i != (len(matrix)-1)):
                danger_level += matrix[index_i+1][index_j]

            if (index_j != 0):
                danger_level += matrix[index_i][index_j-1]

            if (index_j != (len(row)-1)):
                danger_level += matrix[index_i][index_j+1]

            if danger_level < min_danger:
                min_danger = danger_level
                landing_spot = [index_i,index_j]

            danger_level = 0

    return landing_spot

print(find_landing_spot(
    [
    [9, 0, 3], 
    [7, 0, 4], 
    [8, 0, 5]
    ]
    ))