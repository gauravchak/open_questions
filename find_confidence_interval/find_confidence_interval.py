'''
Given a map of values like:
{
  1:0,
  2:5,
  3:20,
  4:10,
  5:3
}
find the smallest interval of keys {min_key, max_key} such that
sum(value[i] for (i >= min_key and i<= max_key) for i in keys)
is more than half the sum of all values.
'''


def find_smallest_interval_sum(list_int: list, min_required_sum: int):
    '''
    Return the indices of the smallest interval where the sum of the numbers is more than min_required_sum
    Given a list of values like [0,5,20,10,3] and a min_required_sum like 19
    find the smallest interval of indices (min_idx, max_idx) such that
    sum(value[i] for (i >= min_idx and i<= max_idx) for i in keys)
    is more than half the sum of all values.
    '''
    # TODO: try to write return value type in the function
    return (0, len(list_int) - 1)


def find_confidence_interval(keys_list: list, values_list: list):
    '''
        Given a map of values like:
        {
            1:0,
            2:5,
            3:20,
            4:10,
            5:3
        }
        find the smallest interval of keys {min_key, max_key} such that
        sum(value[i] for (i >= min_key and i<= max_key) for i in keys)
        is more than half the sum of all values.
    '''
    # TODO: try to write return value type in the function
    min_idx, max_idx = find_smallest_interval_sum(values_list, sum(values_list))
    if ((min_idx < 0) or (max_idx > len(keys_list))):
        return (-1, -1)  # invalid
    else:
        return (keys_list[min_idx], keys_list[max_idx])


def test_find_confidence_interval() -> None:
    '''
    Write a set of test cases and see if the returned tuple of (min_key,max_key) matches the expected answer.
    '''
    test_cases_input = [[[1, 2, 3, 4, 5], [0, 5, 20, 10, 3], (2, 3)]]
    for inp in test_cases_input:
        if (inp and isinstance(inp, list) and (len(inp) == 3)
                and (isinstance(inp[0], list) and isinstance(inp[1], list))):
            out_mink, out_maxk = find_confidence_interval(inp[0], inp[1])
            if ((out_mink, out_maxk) != inp[2]):
                # Output did not match expected output
                raise ValueError('For test case keys:{} values:{} expected output was {} and our output was {}'.format(
                    inp[0], inp[1], inp[2], (out_mink, out_maxk)))
        else:
            print('Ignoring malformed test case {}'.format(inp))
    print('Tests passed')


if __name__ == "__main__":
    test_find_confidence_interval()
