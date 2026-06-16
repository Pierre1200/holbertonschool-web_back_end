#!/usr/bin/env python3
"""
Ce module montre comment encapsuler une coroutine dans une asyncio.Task
en utilisant une fonction synchrone ordinaire.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Prend un délai maximum, crée une coroutine wait_random, l'enveloppe
    dans une asyncio.Task et retourne cet objet Task sans l'attendre.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
