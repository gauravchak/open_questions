#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
from typing import List  # , Tuple


class Intervals:
    def __init__(self, s, e, v):
        self.start_node = s
        self.end_node = e
        self.value = v


# Complete the arrayManipulation function below.
def arrayManipulation(n: int, queries: List[List[int]]):
    intervals = []  # : List[Intervals]
    intervals.append(Intervals(1, n, 0))
    for tq in queries:
        a = tq[0]
        b = tq[1]
        k = tq[2]
        # search first interval index which has overlap with tq
        # search last interval index which has overlap with tq
        for idx, iv in enumerate(intervals):
            pass
    return (0)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
