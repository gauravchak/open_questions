'''
Get the maximum number of boxes that can be stacked with decreasing base length allowing for rotation
Ref: https://www.hackerrank.com/contests/breaking-code/challenges/meth-boxes
Solution: Greedy approach
'''

import os
from typing import List


def rotate_and_remove(boxes: List[List[int]], cur_base_len) -> List[List[int]]:
    newlist = []
    for b in boxes:
        if (max(b[0], b[1]) > cur_base_len):
            # This box can be retained in the new list
            if (min(b[0], b[1]) > cur_base_len):
                # min (b0, b1) is a valid base
                newlist.append([min(b[0], b[1]), max(b[0], b[1])])
            else:
                # max is the only valid base
                newlist.append([max(b[0], b[1]), min(b[0], b[1])])
    if len(boxes) > len(newlist):
        print('rnr diff {} for {}'.format(len(boxes) - len(newlist), cur_base_len))
    return newlist


def get_max_num_boxes(boxes: List[List[int]]) -> int:
    # this is the set of boxes in the top stack built so far
    num_boxes = 0
    # This is the baselen of the top stack built so far
    max_baselen = -1000
    # while there are some boxes left to consider
    # take the box with minimum min (w,h) and remove everything from
    # the list after that which has both coordinates <= this width
    while (boxes):
        # This step ensures that the first coordinate is the smallest acceptable base length
        boxes = rotate_and_remove(boxes, max_baselen)
        # TODO: remove after debugging
        print('Now list of boxes = {}'.format(sorted(boxes)[:10]))
        if not boxes:
            break
        # ncbox is the next chosen box. It has the smallest acceptable base length
        ncbox = min(boxes)  # , key=lambda tb: (tb[0], tb[1]))
        boxes.remove(ncbox)
        num_boxes = num_boxes + 1
        max_baselen = ncbox[0]
        print('Chosen box = {} X {} with max_baselen = {}'.format(ncbox[0], ncbox[1], max_baselen))
    return (num_boxes)


print_to_console = True
if __name__ == '__main__':
    if not print_to_console:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().split()[0])

    gboxes = []

    for _ in range(n):
        gboxes.append(list(map(int, input().rstrip().split())))

    result = get_max_num_boxes(gboxes)
    if print_to_console:
        print(result)
    else:
        fptr.write(str(result) + '\n')
        fptr.close()
