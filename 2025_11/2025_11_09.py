# Word Search
# Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.
# 
# The given matrix will be filled with all lowercase letters (a-z).
# The word to find will always be in the matrix exactly once.
# The word to find will always be in a straight line in one of these directions:
# left to right
# right to left
# top to bottom
# bottom to top
# For example, given the matrix:
# 

def find_word(matrix, word):

        start_possibilities = []
        start = []
        end = []

        for row_index, row in enumerate(matrix):
                for column_index, element in enumerate(row):
                        if element == word[0]:
                                start_possibilities.append([row_index,column_index])

        print(start_possibilities)

        for row, column in start_possibilities:


                result = True
                isFirst = True
                counter = 1

                for character in word:

                        if isFirst:
                                isFirst = False
                                continue

                        try:

                                if matrix[row-counter][column] != word[counter]:
                                        result = False
                                        break

                        except:

                                result = False
                                break

                        counter += 1

                if result != False:
                        counter -= 1
                        start = [row,column]
                        end = [row-counter,column]
                        break


                result = True
                isFirst = True
                counter = 1


                for character in word:

                        if isFirst:
                                isFirst = False
                                continue

                        try:

                                if matrix[row+counter][column] != word[counter]:
                                        result = False
                                        break

                        except:

                                result = False
                                break

                        counter += 1

                if result != False:
                        counter -= 1
                        start = [row,column]
                        end = [row+counter,column]
                        break


                result = True
                isFirst = True
                counter = 1


                for character in word:

                        if isFirst:
                                isFirst = False
                                continue

                        try:

                                if matrix[row][column-counter] != word[counter]:
                                        result = False
                                        break

                        except:

                                result = False
                                break

                        counter += 1

                if result != False:
                        counter -= 1
                        start = [row,column]
                        end = [row,column-counter]
                        break


                result = True
                isFirst = True
                counter = 1


                for character in word:

                        if isFirst:
                                isFirst = False
                                continue

                        try:

                                if matrix[row][column+counter] != word[counter]:
                                        result = False
                                        break

                        except:

                                result = False
                                break

                        counter += 1

                if result != False:
                        counter -= 1
                        start = [row,column]
                        end = [row,column+counter]
                        break
                

        return [start,end]


print(find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat"))