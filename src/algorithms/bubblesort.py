"""
Bubble Sort - Algoritmo de Ordenação por Comparação Adjacente
Complexidade: O(n) melhor caso, O(n²) caso médio e pior caso
"""

def bubblesort(arr: list[int]) -> tuple[list[int], dict]:
    """
    Ordena um array comparando e trocando elementos adjacentes.

    Args:
        arr: Lista de inteiros para ordenar

    Returns:
        Tupla contendo a lista ordenada e dicionário de métricas
    """
    comparisons = 0
    swaps = 0
    len_arr = int(len(arr))

    # Loop externo: percorre n vezes
    for i in range(len_arr):
        # Loop interno: compara elementos adjacentes
        # Reduz tamanho (len_arr-i-1) pois maiores já estão no final
        for j in range(0, len_arr-i-1):
            comparisons += 1

            # Troca se elemento da esquerda > elemento da direita
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return arr, {
        "comparisons": comparisons,
        "swaps": swaps,
        "recursive_calls": 0
    }
