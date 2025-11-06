"""
Merge Sort - Algoritmo de Divisão e Conquista
Complexidade: O(n log n) em todos os casos
Espaço: O(n) - requer arrays temporários
"""

def mergesort(arr: list[int]) -> tuple[list[int], dict]:
    """
    Ordena usando divisão e conquista (divide, ordena, mescla).

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

    def merge(left: list[int], right: list[int]) -> list[int]:
        """Mescla duas listas ordenadas em uma lista ordenada."""
        result = []
        i = j = 0

        # Mescla enquanto ambas têm elementos
        while i < len(left) and j < len(right):
            metrics["comparisons"] += 1

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                metrics["swaps"] += 1  # Conta inversões

        # Adiciona elementos restantes
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(array: list[int]) -> list[int]:
        """Função recursiva do merge sort."""
        # Caso base: array com 0 ou 1 elemento
        if len(array) <= 1:
            return array

        metrics["recursive_calls"] += 1

        # Divide ao meio
        mid = len(array) // 2

        # Conquista: ordena cada metade
        left = merge_sort_recursive(array[:mid])
        right = merge_sort_recursive(array[mid:])

        # Combina: mescla metades ordenadas
        return merge(left, right)

    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, metrics
