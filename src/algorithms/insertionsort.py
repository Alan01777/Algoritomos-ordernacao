"""
Insertion Sort - Algoritmo de Ordenação por Inserção
Complexidade: O(n) melhor caso, O(n²) caso médio e pior caso
"""

def insertionsort(arr: list[int]) -> tuple[list[int], dict]:
    """
    Ordena inserindo cada elemento na posição correta da parte já ordenada.

    Args:
        arr: Lista de inteiros para ordenar

    Returns:
        Tupla contendo a lista ordenada e dicionário de métricas
    """
    comparisons = 0
    swaps = 0
    len_arr = len(arr)

    # Começa do segundo elemento (primeiro já está "ordenado")
    for i in range(1, len_arr):
        key = arr[i]  # Elemento atual a ser inserido
        j = i - 1     # Última posição da parte ordenada

        # Move elementos maiores que key uma posição à direita
        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break  # Encontrou a posição correta

        # Insere key na posição correta
        arr[j + 1] = key

    return arr, {
        "comparisons": comparisons,
        "swaps": swaps,
        "recursive_calls": 0
    }
