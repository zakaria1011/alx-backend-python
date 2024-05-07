#!/usr/bin/env python3
""" The coroutine will collect 10 random numbers """


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ will collect 10 random numbers"""
    random_number = [number async for number in async_generator()]
    return random_number
