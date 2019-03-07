'''
Given a List of Lists like 
[[1, 2, 3, 4],
[1, 3, 5],
[7, 5, 9, 2]]
where [ ... a, b ...] implies that an edge exists from 'a' to 'b'
see if a cycle exists.
'''
import unittest

from typing import List, Dict

class ResourceNode:
    def __init__(self, node_num:int) -> None:
        self.node_num = node_num
        self.color = 0
        self.out_list = set([])

    def add_edge(self, child_node) -> None:
        self.out_list.add(child_node)
    
    def is_in_cycle(self) -> bool:
        if (self.color == 0):
            # if it was white
            self.color = 1  # grey
            for c in self.out_list:
                if c.is_in_cycle():
                    return (True)
            self.color = 2  # black
        if (self.color == 1):
            # if it is grey then there is a cycle
            return (True)
        if (self.color == 2):
            return (False)

def detect_cycle_in_sequence(edge_lists: List[List[int]]) -> bool:
    int_to_node_map: Dict[int, ResourceNode] = {}
    for t_list in edge_lists:
        prev_node = None
        for node_num in t_list:
            # If this node does not exist create it
            if node_num not in int_to_node_map:
                int_to_node_map[node_num] = ResourceNode(node_num)
            cur_node = int_to_node_map[node_num]
            if prev_node is not None:
                prev_node.add_edge(cur_node)
            # Set prev_node for the next iteration of the loop
            prev_node = cur_node
    # # Print graph
    # for c, rn in int_to_node_map.items():
    #     print ('Edges from {} are {}'.format(c, ','.join([str(x.node_num) for x in rn.out_list])))
    for c, rn in int_to_node_map.items():
        if rn.is_in_cycle():
            return (True)
    return (False)

class Test(unittest.TestCase):
    def test_simple_cycle(self):
        x = [[1, 2, 3, 4], [1, 3, 5], [7, 5, 9, 2]]
        actual = detect_cycle_in_sequence(x)
        expected = True
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)