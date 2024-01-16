#!/usr/bin/env python3
""" python_async_comprehension """
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """ aynchronous computation """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
