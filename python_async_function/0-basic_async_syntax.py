#!/usr/bin/env python3
"""
Module for basic async syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire de manière asynchrone et retourne ce délai.

    Args:
        max_delay (int): La borne supérieure du délai d'attente (défaut: 10).

    Returns:
        float: Le temps exact passé en attente durant l'exécution.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
