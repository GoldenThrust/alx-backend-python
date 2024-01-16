#!/usr/bin/env python3
""" python_async_comprehension """
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ aynchronous computation """
    return [i async for i in async_generator()]
