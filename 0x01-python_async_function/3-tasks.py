#!/usr/bin/env python3
"""  asyncro """

import asyncio
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ task wait random  """
    async def wrapper():
        """ wrapper """
        return await wait_random(max_delay)
    return asyncio.create_task(wrapper())
