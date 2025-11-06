"""
Shell Sort - Generalização do Insertion Sort com Gaps
Complexidade: O(n log n) melhor caso, O(n^1.5) médio com Knuth, O(n²) pior caso
Espaço: O(1) - ordena in-place
Usa sequência de gaps de Knuth: h = 3h + 1
"""

def shellsort(arr: list[int]) -> tuple[list[int], dict]:
    """
    Ordena usando insertion sort com gaps decrescentes.

    Args:
        arr: Lista de inteiros para ordenar

    Returns:
        Tupla contendo a lista ordenada e dicionário de métricas
    """
    comparisons = 0
    swaps = 0
    array_copy = arr.copy()
    n = len(array_copy)

    # Calcula gap inicial usando sequência de Knuth (h = 3h + 1)
    # Começa com o maior gap < n/3
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1

    # Loop principal: reduz gap progressivamente até 1
    while gap > 0:
        # Insertion sort com gap atual
        # Ordena elementos que estão "gap" posições distantes
        for i in range(gap, n):
            temp = array_copy[i]
            j = i

            # Move elementos maiores que temp para frente
            while j >= gap:
                comparisons += 1
                if array_copy[j - gap] > temp:
                    array_copy[j] = array_copy[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break

            # Insere temp na posição correta
            if j != i:
                array_copy[j] = temp

        # Reduz gap: (gap - 1) / 3
        gap //= 3

    return array_copy, {
        "comparisons": comparisons,
        "swaps": swaps,
        "recursive_calls": 0  # Shell Sort não é recursivo
    }
