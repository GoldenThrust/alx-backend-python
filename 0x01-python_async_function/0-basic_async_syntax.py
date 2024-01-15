#!/usr/bin/env python3
""" Python - Async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for a random number of seconds to complete """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
