#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#




def mergeHighDefinitionIntervals(intervals):

        old_initial = 0
        old_end = 0
        new_initial = 0
        new_end = 0
        result = []

        for interval in intervals:

                old_initial = new_initial
                new_initial = interval[0]
                old_end = new_end
                new_end = interval[1]

                if new_initial < old_end:
                        new_interval = [old_initial,new_end]
                        result.pop()
                        result.append(new_interval)
                        new_initial = old_initial

                else:
                        result.append(interval)

        return result


def mergeHighDefinitionIntervals(intervals):
       
        if len(intervals) == 0:
               return ""

        integer_list = []

        for interval in intervals:
                for i in range(interval[0],interval[1]+1):
                        if i not in integer_list:
                                integer_list.append(i)

        final_intervals = []
        cached = [integer_list[0]]
        counter = integer_list[0]

        for index, number in enumerate(integer_list):
               
                if index == len(integer_list)-1:
                      cached.append(number)
                      final_intervals.append(cached)
                
                elif number != counter:
                       cached.append(integer_list[index-1])
                       final_intervals.append(cached)
                       cached = [number]
                       counter = number

                counter += 1

        return final_intervals


print(mergeHighDefinitionIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))





if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))