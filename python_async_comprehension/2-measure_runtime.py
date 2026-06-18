#!/usr/bin/env python3
"""
Ce module permet de mesurer le temps d'exécution de tâches asynchrones
lancées de manière concurrente à l'aide d'asyncio.gather.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure le temps d'exécution total de quatre appels simultanés
    à la coroutine async_comprehension lancés en parallèle.
    """

    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    total_time = (end_time - start_time)
    return total_time
