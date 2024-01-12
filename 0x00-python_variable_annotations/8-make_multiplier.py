#!/usr/bin/env python3
""" python variable anotation """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make a multiplier function """
    return lambda x: x * multiplier
