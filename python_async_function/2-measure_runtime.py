#!/usr/bin/env python3
"""
Ce module permet de mesurer le temps d'exécution d'une routine asynchrone.
Il démontre l'efficacité de la concurrence par le calcul du temps moyen.
"""
import asyncio
import time

# Importation dynamique de la fonction de la tâche 1
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution total de wait_n et renvoie le temps
    moyen par tâche (temps total divisé par n).
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = (end_time - start_time) / n
    return total_time
