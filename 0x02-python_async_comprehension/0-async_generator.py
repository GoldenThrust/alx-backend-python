#!/usr/bin/env python3
""" python_async_comprehension """
import random
import asyncio
from typing import Iterator


async def async_generator() -> Iterator[int]:
    """ asynchronous generator """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
