#!/usr/bin/env python3
""" sum of int and float """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ mixed sum """
    return sum(mxd_lst)
