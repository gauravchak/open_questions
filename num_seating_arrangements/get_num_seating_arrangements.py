'''
Given a row count N
and N strings like:
EET|EEET|EEE
find the number of seating arrangements of a family of 3
'''
from typing import List


class InvalidArguments(Exception):
    '''Number of rows does not match the length of the list of strings'''
    pass


factmap: dict = {}


def factorial(n: int) -> int:
    if n in factmap:
        return factmap[n]
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        retval = factorial(n - 1) * n
        factmap[n] = retval
        return retval


def get_num_seating_arrangements_in_row(num_together: int, row_str: str) -> int:
    i = 0
    num_empty_in_zone = 0
    retval = 0
    while (i < len(row_str)):
        if row_str[i] == 'E':
            num_empty_in_zone = num_empty_in_zone + 1
        elif row_str[i] != '|':
            if num_empty_in_zone >= num_together:
                retval = retval + (factorial(num_empty_in_zone) //
                                   (factorial(num_together) * factorial(num_empty_in_zone - num_together)))
            num_empty_in_zone = 0
        i = i + 1
    if num_empty_in_zone >= num_together:
        retval = retval + (factorial(num_empty_in_zone) //
                           (factorial(num_together) * factorial(num_empty_in_zone - num_together)))
    return retval


def get_num_seating_arrangements(N: int, num_together: int, rows: List[str]) -> int:
    if len(rows) != N:
        raise InvalidArguments
    retval = 0
    for row_str in rows:
        retval = retval + get_num_seating_arrangements_in_row(num_together, row_str)
    return retval
