"""
Funções para geração de arrays de teste
"""
import random


def generate_random_array(size: int, lower_bound: int, upper_bound: int) -> list[int]:
    """
    Gera um array aleatório de inteiros

    Args:
        size: Tamanho do array
        lower_bound: Limite inferior dos valores
        upper_bound: Limite superior dos valores

    Returns:
        Lista de inteiros aleatórios
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def generate_ordered_array(size: int) -> list[int]:
    """
    Gera um array ordenado de inteiros

    Args:
        size: Tamanho do array

    Returns:
        Lista de inteiros ordenados (1 até size)
    """
    return list(range(1, size + 1))


def generate_reverse_ordered_array(size: int) -> list[int]:
    """
    Gera um array ordenado em ordem reversa

    Args:
        size: Tamanho do array

    Returns:
        Lista de inteiros ordenados em ordem reversa (size até 1)
    """
    return list(range(size, 0, -1))
