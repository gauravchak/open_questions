from typing import List


def get_max_triproduct(int_list: List[int]) -> int:
    '''
    Method:
    Separate list into positive and negative numbers
    Among negative numbers get the bottom two min_neg, pen_min_neg.
    Among positive numbers get the top three numbers pos_1_top, pos_2, pos_3.
    neg_biproduct = min_neg * pen_min_neg
    pos_pen_biproduct = pos_2 * pos_3
    Then return pos_1_top * max( neg_biproduct, pos_pen_biproduct)
    i.e. max (pos_1_top * pos_2 * pos_3, pos_1_top * min_neg * pen_min_neg)
    '''
    min_neg = 0
    pen_min_neg = 0
    pos_1_top = 0
    pos_2 = 0
    pos_3 = 0
    for this_int in int_list:
        if (this_int < 0):
            if (this_int < min_neg):
                pen_min_neg = min_neg
                min_neg = this_int
            elif (this_int < pen_min_neg):
                pen_min_neg = this_int
        else:
            if (this_int > pos_3):
                if (this_int > pos_2):
                    if (this_int > pos_1_top):
                        pos_3 = pos_2
                        pos_2 = pos_1_top
                        pos_1_top = this_int
                    else:
                        pos_3 = pos_2
                        pos_2 = this_int
                else:
                    pos_3 = this_int
    neg_biproduct = min_neg * pen_min_neg
    pos_pen_biproduct = pos_2 * pos_3
    max_tp = pos_1_top * max(neg_biproduct, pos_pen_biproduct)
    return max_tp
