'''
Input:
       screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };
    x = 4, y = 4, newColor = 3
The values in the given 2D screen indicate colors of the pixels.
x and y are coordinates of the brush, newColor is the color that
should replace the previous color on screen[x][y] and all surrounding
pixels with same color.

Output:
Screen should be changed to following.
       screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 3, 3, 3, 3, 0, 1, 0},
                      {1, 1, 1, 3, 3, 0, 1, 0},
                      {1, 1, 1, 3, 3, 3, 3, 0},
                      {1, 1, 1, 1, 1, 3, 1, 1},
                      {1, 1, 1, 1, 1, 3, 3, 1},
                      };
'''
import unittest
from typing import List


class Screen:
    def __init__(self, scr_ar: List[List[int]]) -> None:
        self.numrows = len(scr_ar)
        self.numcols = len(scr_ar[0])
        self.ar = scr_ar

    def flood_fill(self, rowidx: int, colidx: int, newColor: int, cur_color=None) -> None:
        if ((cur_color is None) or (self.ar[rowidx][colidx] == cur_color)) and (self.ar[rowidx][colidx] != newColor):
            if (cur_color is None):
                cur_color = self.ar[rowidx][colidx]
            self.ar[rowidx][colidx] = newColor
            for delr, delc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = rowidx + delr
                new_c = colidx + delc
                if (new_r >= 0 and new_r < self.numrows) and (new_c >= 0 and new_c < self.numcols):
                    self.flood_fill(rowidx=new_r, colidx=new_c, newColor=newColor, cur_color=cur_color)

    def __str__(self):
        return ('\n'.join([' '.join([str(y) for y in x]) for x in self.ar]))


class Tests(unittest.TestCase):
    def test_simple(self):
        scr_vals = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1],
                    [1, 2, 2, 2, 2, 0, 1, 0], [1, 1, 1, 2, 2, 0, 1, 0], [1, 1, 1, 2, 2, 2, 2, 0],
                    [1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 2, 2, 1]]
        scr = Screen(scr_vals)
        # print(str(scr))
        x = 4
        y = 4
        newColor = 3
        scr.flood_fill(x - 1, y - 1, newColor)
        exp_scr_vals = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1],
                        [1, 3, 3, 3, 3, 0, 1, 0], [1, 1, 1, 3, 3, 0, 1, 0], [1, 1, 1, 3, 3, 3, 3, 0],
                        [1, 1, 1, 1, 1, 3, 1, 1], [1, 1, 1, 1, 1, 3, 3, 1]]
        self.assertListEqual(exp_scr_vals, scr.ar)


unittest.main(verbosity=2)