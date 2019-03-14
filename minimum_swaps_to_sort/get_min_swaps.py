#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

from typing import List


def find_steepest_fall(arr: List[int]) -> int:
    if not arr:
        return 0
    si = 0
    selem = arr[si]
    ei = 0
    eelem = arr[ei]
    # These are global maxes
    sf = 0
    msi = si
    mei = ei
    # Loop over all elements
    for idx, elem in enumerate(arr):
        if (elem < eelem):
            ei = idx
            eelem = elem
            if (sf < (selem - eelem)):
                sf = (selem - eelem)
                msi = si
                mei = ei
        if (elem > selem):
            # start again
            si = idx
            selem = elem
            ei = idx
            eelem = elem
    return (msi, mei, sf)


def minimumSwapsGreedy(arr, debug_=False) -> int:
    min_swaps = 0
    i, j, f = find_steepest_fall(arr)
    if debug_:
        print("DBG i j f = {} {} {}".format(i, j, f))
    while (f > 0):
        if debug_:
            print("DBG Swapping {} & {} since f = {}".format(i, j, f))
        t = arr[i]  # saved value to swap
        arr[i] = arr[j]
        arr[j] = t
        min_swaps = (min_swaps + 1)
        i, j, f = find_steepest_fall(arr)
        if debug_:
            print("DBG i j f = {} {} {}".format(i, j, f))
    return (min_swaps)


def minimumSwaps(arr, debug_=False) -> int:
    min_swaps = 0
    # setup edges in graph
    edges_ = {}
    # a map to mark nodes seen
    seen_ = {}
    for idx, arrval in enumerate(arr):
        node_num = idx + 1
        edges_[node_num] = arrval
        seen_[node_num] = False
    # find cycle lengths
    for idx, arrval in enumerate(arr):
        node_num = idx + 1
        current_node = node_num
        if not seen_[current_node]:
            # unseen node. Hence this might be a cycle
            cycle_len = 1
            seen_[current_node] = True
            while (edges_[current_node] != node_num):
                cycle_len = cycle_len + 1
                current_node = edges_[current_node]
                seen_[current_node] = True
            # sum (cycle lengths - 1)
            min_swaps = min_swaps + (cycle_len - 1)
    return (min_swaps)


def process_input():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)


if __name__ == '__main__':
    process_input()