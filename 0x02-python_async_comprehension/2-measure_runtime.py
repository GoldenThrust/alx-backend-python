#!/usr/bin/env python3
""" python_async_comprehension """
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the runtime of the computation """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return (time.perf_counter() - start)
