import os
os.system("cls")


def rotate(matrix):

    i=0
    j=0
    i_add=(len(matrix)-1)
    j_add=-1

    value_list=[]
    temp_dict={}
    temp_dict2={}
    

    for row in matrix:

        i+=1
        j=0
        j_add += 1
        i_add=(len(matrix)-1)

        for col in row:

            j+=1
            temp_dict[i,j]=matrix[(i_add)][(j_add)]
            i_add -= 1
            value_list.append(temp_dict[i,j])

    i=0
    j=len(matrix)

    for i in range(0, len(value_list), j):
        temp_dict2[i] = value_list[i:i + j]
        
    new_matrix=list(temp_dict2.values())

    return new_matrix

print(rotate([[1,2],[3,4]]))