"""
Funções para medição de desempenho de algoritmos
"""
import timeit
import tracemalloc
from typing import Callable


def measure_algorithm(algorithm: Callable, arr: list[int], array_type: str = 'random') -> tuple[list[int], dict]:
    """
    Mede o desempenho de um algoritmo de ordenação

    Args:
        algorithm: Função do algoritmo de ordenação
        arr: Array para ordenar
        array_type: Tipo do array ('random', 'ordered', 'reverse')

    Returns:
        Tupla contendo:
        - Lista ordenada
        - Dicionário com métricas completas (comparisons, swaps, execution_time, memory_usage, array_type)
    """
    start = timeit.default_timer()
    tracemalloc.start()

    ordered_arr, metrics = algorithm(arr.copy())

    time = timeit.default_timer() - start
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return ordered_arr, {
        **metrics,
        "execution_time": time,
        "memory_usage": memory,
        "array_type": array_type
    }
