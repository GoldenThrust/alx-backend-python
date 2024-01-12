#!/usr/bin/env python3
""" python variable anotation """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return k and v as tuple """
    return (k, v**2)
