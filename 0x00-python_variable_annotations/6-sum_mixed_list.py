#!/usr/bin/env python3
""" python variable anotation """
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """ return the sum of mxd_lst """
    return sum(mxd_lst)
