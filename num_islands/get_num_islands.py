'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
'''

import unittest
from typing import List


class Graph:
    '''
    This is used to run a depth first search of the island
    '''

    def __init__(self, num_rows, num_cols, mval: List[List[int]]) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.mval = mval
        self.color = [[0] * num_cols for x in range(num_rows)]

    def color_this_island_black(self, r, c) -> None:
        '''This changes the color list value for the given index and every other index reachable from it'''
        self.color[r][c] = 1
        for dr, dc in [(-1, 0), (-1, 0), (0, 1), (1, 0)]:
            new_r = (r + dr)
            new_c = (c + dc)
            if ((new_r >= 0) and (new_r < self.num_rows) and (new_c >= 0) and (new_c < self.num_cols)):
                # valid index
                if (self.color[new_r][new_c] == 0) and (self.mval[new_r][new_c] == 1):
                    # if it is land and it is white then
                    self.color_this_island_black(new_r, new_c)

    def __str__(self):
        '''For printing'''
        ret_str = '\n'.join([' '.join([str(y) for y in x]) for x in self.mval])
        return (ret_str)

    def get_num_islands(self) -> int:
        num_islands = 0
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if (self.color[r][c] == 0) and (self.mval[r][c] == 1):
                    # there is lands and it is still white
                    # increment the counter
                    num_islands = num_islands + 1
                    # color_this_island
                    self.color_this_island_black(r, c)
        return (num_islands)


def get_num_islands(mval: List[List[int]]) -> int:
    num_rows = len(mval)
    num_cols = len(mval[0])
    if num_rows < 1:
        return (0)
    if num_cols < 1:
        return (0)
    if len(set([len(x) for x in mval])) != 1:
        raise ValueError('num cols dont match')
        return (0)
    g = Graph(num_rows, num_cols, mval)
    return (g.get_num_islands())


class Tests(unittest.TestCase):
    def test_1(self):
        mval = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        expected = 1
        actual = get_num_islands(mval)
        self.assertEqual(expected, actual)


unittest.main(verbosity=2)