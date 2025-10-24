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

print(mergeHighDefinitionIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))


if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))