import unittest
from typing import List, Dict


def add_char_to_str_list(c: str, substr_list: List[str]) -> List[str]:
    return [c + x for x in substr_list]


def get_t9_words(num_str: str) -> List[str]:
    '''

    '''
    t9exp: Dict[str, List[str]] = {
        '0': [],
        '1': [],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y'],
    }
    # 0 length input string
    if not num_str:
        return []
    numc = num_str[0]
    # 1 length input string
    if len(num_str) == 1:
        if numc in t9exp:
            # this is a valid character
            return (t9exp[numc])
        else:
            return []
    substr_list = get_t9_words(num_str[1:])
    if not substr_list:
        # if somehow the remaining list is empty then
        if numc in t9exp:
            return (t9exp[numc])
        else:
            return []
    # remaining list is non empty
    if numc in t9exp:
        t_list = t9exp[numc]
        if not t_list:
            return (substr_list)
        else:
            ret_list: List[str] = []
            for c in t_list:
                ret_list.extend(add_char_to_str_list(c, substr_list))
            return (ret_list)
    else:
        return (substr_list)


class Tests(unittest.TestCase):
    def test_1(self):
        mval = {
            "28": ["AT", "AU", "AV", "BT", "BU", "BV", "CT", "CU", "CV"],
            "22": ["AA", "AB", "AC", "BA", "BB", "BC", "CA", "CB", "CC"],
            "223": [
                'AAD', 'AAE', 'AAF', 'ABD', 'ABE', 'ABF', 'ACD', 'ACE', 'ACF', 'BAD', 'BAE', 'BAF', 'BBD', 'BBE', 'BBF',
                'BCD', 'BCE', 'BCF', 'CAD', 'CAE', 'CAF', 'CBD', 'CBE', 'CBF', 'CCD', 'CCE', 'CCF'
            ]
        }
        for k, expected in mval.items():
            actual = get_t9_words(k)
            self.assertListEqual(expected, actual)


unittest.main(verbosity=2)