#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments. """

import asyncio
import random


async def async_generator():
    """ generate 10 random values"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

