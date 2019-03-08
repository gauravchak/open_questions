from typing import List

class Interval:
    '''
    Definition for an interval
    '''
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key = lambda x: x.start)
        out_list = []
        for t_i in intervals:
            if ((len(out_list) == 0) or (t_i.start > out_list[-1].end)):
                # either the out list is empty 
                # or the start time of the next interval is less 
                # than the end time of the current last interval
                # then there is no overlap and hence we need to add a new one
                out_list.append(t_i)
            else:
                # if the new interval is overlapping with the currently 
                # last interval in the out_list then 
                # we should update the end time of the current last
                out_list[-1].end = max ( out_list[-1].end, t_i.end )
        return (out_list)