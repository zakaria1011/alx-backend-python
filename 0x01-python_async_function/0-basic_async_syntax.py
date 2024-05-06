#!/usr/bin/env python3
""" basic adync syntax """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ coroutine that delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
