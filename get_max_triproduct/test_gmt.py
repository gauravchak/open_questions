from typing import List
from get_max_triproduct import get_max_triproduct

if __name__ == "__main__":
    list_of_ints: List[int] = [1, 10, -5, 1, -100]
    if (len(list_of_ints) < 3):
        raise ValueError('List needs to have at least 3 numbers')
    result: int = get_max_triproduct(list_of_ints)
    print('Max tri product computed = {}'.format(result))
