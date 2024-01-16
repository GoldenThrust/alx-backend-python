#!/usr/bin/env python3
""" python_async_comprehension """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ asynchronous generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
