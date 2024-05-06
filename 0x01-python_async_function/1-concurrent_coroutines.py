#!/usr/bin/env python3
""" multiple coroutine at the same time """


import asyncio
from typing import List
from asyncio import gather

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async coroutine that execute multple coroutine"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await gather(*coroutines)
    return sorted(results)
