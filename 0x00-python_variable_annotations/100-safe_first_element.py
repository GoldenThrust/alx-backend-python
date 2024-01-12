#!/usr/bin/env python3
""" python variable anotation """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe_first element of the input sequence """
    if lst:
        return lst[0]
    else:
        return None
