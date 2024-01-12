#!/usr/bin/env python3
""" python variable anotation """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    iterate over the elements of lst and
    return the length of each element """
    return [(i, len(i)) for i in lst]
