'''
Given a hexagonal tile game, where there is a letter on each tile, write an algorithm to determine
if a given word exists by traversing the graph without repeatedly visiting nodes.
'''
from typing import Tuple, List #, Dict

class WrongArgException(Exception):
    pass

rev_index_map = {0:3, 1:4, 2:5, 3:0, 4:1, 5:2}

class HexGame:
    def __init__(self, tile_edges: List[Tuple[int, int, int]], tile_chars: List[str]) -> None:
        self.hextile_list = []
        for idx, mychar in enumerate(tile_chars):
            self.hextile_list.append(HexTile(idx + 1, mychar))
        for x in tile_edges:
            root_node = self.hextile_list[x[0] - 1]  # the reference to the staring node of this edge
            out_idx = x[1] - 1  # out_idx = index in self.out_tile_list
            child_node = self.hextile_list[x[2] - 1]  # the reference to the ending node of this edge
            # print ('MAINDEBUG set_edge {} {} {}'.format(root_node.tile_num, out_idx, child_node.tile_num))
            root_node.set_edge(out_idx, child_node)

    def search_string(self, str_to_find:str) -> bool:
        '''Search if the given string exists in some node traversal which does not visit the same edge twice'''
        # make a list of nodes where the first character matches
        # tmfc := tiles_matching_first_char
        tmfc = [x for x in self.hextile_list if x.search_string(str_to_find, 0, [False]*len(self.hextile_list))]
        # for each of them search the given substring after resetting the seen value of nodes
        if tmfc:
            return True
        else:
            return False

    def print_game(self) -> None:
        for x in self.hextile_list:
            print ('{} -> {}'.format(x.tile_char, ','.join([c.tile_char if c else '-' for c in x.out_tile_list])))

class HexTile:
    '''
    A single tile.
    It has outgoing edges
    '''
    def __init__(self, tile_num:int, mychar:str):
        if len(mychar) != 1:
            raise WrongArgException
        self.tile_num = tile_num
        self.tile_char = mychar
        self.out_tile_list = [None] * 6

    def set_edge(self, out_idx:int, child_node) -> None:
        if child_node is None:
            return
        if (out_idx < 0 or out_idx >= 6):
            raise WrongArgException
        if (self.out_tile_list[out_idx] == child_node):
            # This has been set already, hence nothing to do
            return
        # print ('DEBUG set_edge {} {} {}'.format(self.tile_char, out_idx, child_node.tile_char))
        self.out_tile_list[out_idx] = child_node
        # Set reverse
        # For A 0 B
        # Set B[3] = A
        rev_idx = rev_index_map[out_idx]
        child_node.set_edge(rev_idx, self)
        # Set B's neighbors if mine are known
        # Set B[(3-1)%6] = A[(0+1)%6]
        if self.out_tile_list[(out_idx+1)%6] is not None:
            child_node.set_edge((rev_idx-1)%6, self.out_tile_list[(out_idx+1)%6])
        # Set B[(3+1)%6] = A[(0-1)%6]
        if self.out_tile_list[(out_idx-1)%6] is not None:
            child_node.set_edge((rev_idx+1)%6, self.out_tile_list[(out_idx-1)%6])
        # Set my neighbors from B's if mine are not known and B's are
        # Set A[(0+1)%6] = B[(3-1)%6]
        if ((child_node.out_tile_list[(rev_idx-1)%6] is not None) and (self.out_tile_list[(out_idx+1)%6] is None)):
            self.set_edge((out_idx+1)%6, child_node.out_tile_list[(rev_idx-1)%6])
        # Set A[(0-1)%6] = B[(3+1)%6]
        if ((child_node.out_tile_list[(rev_idx+1)%6] is not None) and (self.out_tile_list[(out_idx-1)%6] is None)):
            self.set_edge((out_idx-1)%6, child_node.out_tile_list[(rev_idx+1)%6])

    def search_string(self, str_to_find:str, char_idx:int, seen_list:List[bool]) -> bool:
        # If this node has been seen already then return saying no substring found that matches
        if seen_list[self.tile_num-1]:
            return False
        # It is not expected that we call with an empty string but if could happen at root of the call
        if not str_to_find:
            return True
        # This is also not expected that we call with an empty string but if could happen at root of the call
        if (char_idx >= len(str_to_find)):
            return True
        # if this does not match the 
        if (self.tile_char != str_to_find[char_idx]):
            return False
        else:
            seen_list[self.tile_num - 1] = True
            if (char_idx + 1 >= len(str_to_find)):
                return True
            else:
                for c in self.out_tile_list:
                    if c:
                        if c.search_string(str_to_find, char_idx+1, seen_list):
                            return True  # A true signal cascades up quickly
                # if all false then set seen to false so that we can use this node in another path and return false
                seen_list[self.tile_num - 1] = False
                return False


def find_substring(tile_edges: List[Tuple[int, int, int]], tile_chars: List[str], str_to_find: str) -> bool:
    hg = HexGame(tile_edges, tile_chars)
    # For debugging ... hg.print_game()
    return (hg.search_string(str_to_find))
