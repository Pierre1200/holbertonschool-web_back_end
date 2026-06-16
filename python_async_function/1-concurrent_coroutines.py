#!/usr/bin/env python3
"""
Module for basic async syntax
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance n fois la coroutine wait_random en même temps et retourne
    la liste des délais générés, triée de manière croissante grâce
    au cycle de complétion asynchrone.
    """
    delays: List[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
