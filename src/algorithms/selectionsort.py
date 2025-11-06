"""
Selection Sort - Algoritmo de Ordenação por Seleção
Complexidade: O(n²) em todos os casos (melhor, médio e pior)
Característica: Minimiza número de trocas (apenas n)
"""

def selectionsort(arr: list[int]) -> tuple[list[int], dict]:
    """
    Ordena selecionando repetidamente o menor elemento.

    Args:
        arr: Lista de inteiros para ordenar

    Returns:
        Tupla contendo a lista ordenada e dicionário de métricas
    """
    comparisons = 0
    swaps = 0
    len_arr = len(arr)

    # Para cada posição do array
    for i in range(len_arr):
        min_idx = i  # Assume que o primeiro não ordenado é o menor

        # Procura o menor elemento no restante
        for j in range(i + 1, len_arr):
            comparisons += 1

            if arr[j] < arr[min_idx]:
                min_idx = j  # Atualiza índice do menor

        # Troca apenas se encontrou algo menor
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, {
        "comparisons": comparisons,
        "swaps": swaps,
        "recursive_calls": 0
    }
