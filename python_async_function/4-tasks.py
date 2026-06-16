#!/usr/bin/env python3
"""
Ce module permet d'exécuter plusieurs objets asyncio.Task en même temps.
brique de création de tâche synchrone pour gérer la concurrence.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance n fois la fonction task_wait_random en même temps et retourne
    la liste des délais générés, triée de manière croissante grâce
    au cycle de complétion asynchrone.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
