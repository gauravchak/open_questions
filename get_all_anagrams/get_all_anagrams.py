'''
Write a program to find anagrams in a set of letters that uses all of the letters.
'''

import unittest
from typing import List


def add_char_to_all_pos_in_str(c: str, t_item: str) -> List[str]:
    '''
    1. For c = 'A' and t_item = 'BCD'
    return ['ABCD', 'BACD', 'BCAD', 'BCDA']
    2. For c = 'A' and t_item = 'ACD'
    return ['AACD', 'ACAD', 'ACDA']
    '''
    ret_list = []
    for i in range(len(t_item)):
        if (t_item[i] != c):
            ret_list.append(t_item[:i] + c + t_item[i:])
    ret_list.append(t_item + c)
    return (ret_list)


def get_all_anagrams(src: str) -> List[str]:
    if not src:
        return ([])
    sublist: List[str] = get_all_anagrams(src[1:])
    if not sublist:
        return ([src[0]])
    retlist = []
    for t_item in sublist:
        t_list = add_char_to_all_pos_in_str(src[0], t_item)
        retlist.extend(t_list)
    return (retlist)


class Tests(unittest.TestCase):
    def test1(self):
        cases = {
            'a': ['a'],
            'ab': ['ab', 'ba'],
            'aa': ['aa'],
            'abcd': [
                'abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc',
                'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba'
            ]
        }
        for src, expected in cases.items():
            actual = get_all_anagrams(src)
            self.assertListEqual(actual, expected)


unittest.main(verbosity=2)