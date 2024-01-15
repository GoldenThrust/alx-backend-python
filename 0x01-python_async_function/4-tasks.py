#!/usr/bin/env python3
""" Python - Async """
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a given number of seconds to complete before
    returning immediately
    """
    return sorted(await asyncio.gather(*(task_wait_random(max_delay)
                                         for _ in range(n))))
