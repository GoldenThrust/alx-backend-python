#!/usr/bin/env python3
""" Python - Async """
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a given number of seconds to complete before
    returning immediately
    """
    return sorted(await asyncio.gather(*(wait_random(max_delay)
                                         for _ in range(n))))
