'''
Given a hexagonal tile game, where there is a letter on each tile, write an algorithm to determine
if a given word exists by traversing the graph without repeatedly visiting nodes.
'''
from typing import Tuple, List, Dict


def find_substring(tiles: List[Tuple[int, int, int]], tile_chars: Dict[int, str], str_to_find: str) -> bool:
    return False