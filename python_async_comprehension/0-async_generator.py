#!/usr/bin/env python3
"""
Ce module introduit le concept de générateur asynchrone en Python.
Il permet de produire des flux de données à intervalles réguliers.
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Génère des nombres aléatoires de manière asynchrone.

    Yields:
        float: Un nombre aléatoire entre 0 et 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
