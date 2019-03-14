from typing import List
import unittest


def get_all_paren_str_frm_prefix(pfx: str, max_par: int, num_open: int, num_closed: int,
                                 num_stack_open: int) -> List[str]:
    '''Tries to add the next character and then call itself recursively'''
    str_list: List[str] = []
    if (num_stack_open > 0):
        # closing a bracket is an option
        str_list = str_list + get_all_paren_str_frm_prefix(pfx + ')', max_par, num_open, num_closed + 1,
                                                           num_stack_open - 1)

    if (num_open < max_par):
        str_list = str_list + get_all_paren_str_frm_prefix(pfx + '(', max_par, num_open + 1, num_closed,
                                                           num_stack_open + 1)

    if (num_open == max_par) and (num_closed == max_par):
        str_list = [pfx]
    return (str_list)


def get_all_paren_strings(n: int) -> List[str]:
    '''Returns a list of strings each with n parentheses

    Methodology:
    Constructs valid paren strings
    '''
    str_list: List[str] = get_all_paren_str_frm_prefix('', n, 0, 0, 0)
    return (str_list)


class Tests(unittest.TestCase):
    def test_1(self):
        num_parens: int = 4
        actual = get_all_paren_strings(num_parens)
        expected = [
            '()()()()', '()()(())', '()(())()', '()(()())', '()((()))', '(())()()', '(())(())', '(()())()', '(()()())',
            '(()(()))', '((()))()', '((())())', '((()()))', '(((())))'
        ]
        self.assertListEqual(actual, expected)


unittest.main(verbosity=2)