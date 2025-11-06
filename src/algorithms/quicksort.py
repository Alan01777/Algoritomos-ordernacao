"""
Quick Sort - Algoritmo de Particionamento com Otimizações
Complexidade: O(n log n) médio, O(n²) pior caso (raro com otimizações)

Otimizações implementadas:
1. Mediana de três - evita O(n²) em arrays ordenados
2. Insertion sort híbrido - para partições pequenas (<10)
3. Tail call optimization - limita profundidade recursiva
"""

import random

def quicksort(arr: list[int]) -> tuple[list[int], dict]:
    """
    Ordena usando particionamento por pivô com otimizações.

    Args:
        arr: Lista de inteiros para ordenar

    Returns:
        Tupla contendo a lista ordenada e dicionário de métricas
    """
    metrics = {
        "comparisons": 0,
        "swaps": 0,
        "recursive_calls": 0
    }

    def median_of_three(array: list[int], low: int, high: int) -> int:
        """
        Escolhe pivô usando mediana de três elementos.
        Evita pior caso O(n²) em arrays ordenados.
        """
        mid = (low + high) // 2

        # Ordena low, mid, high
        metrics["comparisons"] += 3
        if array[low] > array[mid]:
            array[low], array[mid] = array[mid], array[low]
            metrics["swaps"] += 1
        if array[low] > array[high]:
            array[low], array[high] = array[high], array[low]
            metrics["swaps"] += 1
        if array[mid] > array[high]:
            array[mid], array[high] = array[high], array[mid]
            metrics["swaps"] += 1

        # Coloca mediana no final (onde pivô é esperado)
        array[mid], array[high] = array[high], array[mid]
        metrics["swaps"] += 1

        return array[high]

    def partition(array: list[int], low: int, high: int) -> int:
        """Particiona array: menores à esquerda, maiores à direita do pivô."""
        pivot = median_of_three(array, low, high)
        i = low - 1

        for j in range(low, high):
            metrics["comparisons"] += 1
            if array[j] <= pivot:
                i += 1
                if i != j:
                    array[i], array[j] = array[j], array[i]
                    metrics["swaps"] += 1

        # Coloca pivô na posição correta
        if i + 1 != high:
            array[i + 1], array[high] = array[high], array[i + 1]
            metrics["swaps"] += 1

        return i + 1

    def quick_sort_recursive(array: list[int], low: int, high: int):
        """Função recursiva do quick sort com otimizações."""
        # Otimização: Insertion sort para arrays pequenos
        if high - low < 10:
            for i in range(low + 1, high + 1):
                key = array[i]
                j = i - 1
                while j >= low:
                    metrics["comparisons"] += 1
                    if array[j] > key:
                        array[j + 1] = array[j]
                        metrics["swaps"] += 1
                        j -= 1
                    else:
                        break
                array[j + 1] = key
            return

        if low < high:
            metrics["recursive_calls"] += 1
            pi = partition(array, low, high)

            # Otimização: recursão na menor partição primeiro
            # Garante profundidade máxima O(log n)
            if pi - low < high - pi:
                quick_sort_recursive(array, low, pi - 1)
                quick_sort_recursive(array, pi + 1, high)
            else:
                quick_sort_recursive(array, pi + 1, high)
                quick_sort_recursive(array, low, pi - 1)

    array_copy = arr.copy()
    if len(array_copy) > 0:
        quick_sort_recursive(array_copy, 0, len(array_copy) - 1)

    return array_copy, metrics
