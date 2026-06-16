#!/usr/bin/env python3
"""
Ce module montre comment utiliser les compréhensions de liste asynchrones.
Il permet de condenser la consommation d'un générateur asynchrone.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte les 10 nombres générés par async_generator en utilisant
    une expression de compréhension asynchrone et les retourne.
    """
    return [i async for i in async_generator()]
