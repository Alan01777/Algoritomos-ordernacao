"""
Hub Universal para Algoritmos de Ordenação
Executa testes de desempenho e gera métricas em CSV
"""
from algorithms import (
    bubblesort,
    insertionsort,
    selectionsort,
    mergesort,
    quicksort,
    shellsort
)
from utils import (
    generate_random_array,
    generate_ordered_array,
    generate_reverse_ordered_array,
    measure_algorithm,
    save_metrics_to_csv
)


# Dicionário de algoritmos disponíveis
AVAILABLE_ALGORITHMS = {
    'bubblesort': bubblesort,
    'insertionsort': insertionsort,
    'selectionsort': selectionsort,
    'mergesort': mergesort,
    'quicksort': quicksort,
    'shellsort': shellsort,
}


def run_algorithm_tests(algorithm_name: str, sizes: list[int], lower_bound: int = 1, upper_bound: int = 10000):
    """
    Executa testes de um algoritmo específico com diferentes tamanhos de array

    Args:
        algorithm_name: Nome do algoritmo a ser testado
        sizes: Lista de tamanhos de arrays para testar
        lower_bound: Limite inferior para valores aleatórios
        upper_bound: Limite superior para valores aleatórios

    Returns:
        Lista de métricas coletadas
    """
    if algorithm_name not in AVAILABLE_ALGORITHMS:
        print(f"Algoritmo '{algorithm_name}' não encontrado!")
        print(f"Algoritmos disponíveis: {', '.join(AVAILABLE_ALGORITHMS.keys())}")
        return []

    algorithm = AVAILABLE_ALGORITHMS[algorithm_name]
    all_metrics = []

    print(f"\n{'='*60}")
    print(f"Testando algoritmo: {algorithm_name.upper()}")
    print(f"{'='*60}")

    for size in sizes:
        print(f"\nProcessando array de tamanho {size}...")

        # Gerar os três tipos de arrays
        arrays_to_test = [
            ('random', generate_random_array(size, lower_bound, upper_bound)),
            ('ordered', generate_ordered_array(size)),
            ('reverse', generate_reverse_ordered_array(size))
        ]

        # Testar cada tipo de array
        for array_type, array in arrays_to_test:
            print(f"  Tipo: {array_type}")
            _, metrics = measure_algorithm(algorithm, array, array_type)

            metrics['algorithm'] = algorithm_name
            metrics['array_size'] = size
            all_metrics.append(metrics)

            print(f"    Comparações: {metrics['comparisons']}")
            print(f"    Trocas: {metrics['swaps']}")
            print(f"    Chamadas Recursivas: {metrics['recursive_calls']}")
            print(f"    Tempo de Execução: {metrics['execution_time']:.6f} segundos")
            print(f"    Uso de Memória: Atual={metrics['memory_usage'][0]} bytes, Pico={metrics['memory_usage'][1]} bytes")

    return all_metrics


def run_all_algorithms(sizes: list[int], lower_bound: int = 1, upper_bound: int = 10000):
    """
    Executatodos os algoritmos disponíveis

    Args:
        sizes: Lista de tamanhos de arrays para testar
        lower_bound: Limite inferior para valores aleatórios
        upper_bound: Limite superior para valores aleatórios

    Returns:
        Lista de todas as métricas coletadas
    """
    all_metrics = []

    for algorithm_name in AVAILABLE_ALGORITHMS.keys():
        metrics = run_algorithm_tests(algorithm_name, sizes, lower_bound, upper_bound)
        all_metrics.extend(metrics)

    return all_metrics


def main():
    """Função principal - "Hub" de execução de algoritmos"""
    sizes = [10, 100, 1000, 10000]
    lower_bound = 1
    upper_bound = 10000

    print("="*60)
    print("HUB UNIVERSAL DE ALGORITMOS DE ORDENAÇÃO")
    print("="*60)
    print(f"\nAlgoritmos disponíveis: {', '.join(AVAILABLE_ALGORITHMS.keys())}")
    print(f"Tamanhos de teste: {sizes}")
    print(f"Tipos de array: random, ordered, reverse")

    all_metrics = run_all_algorithms(sizes, lower_bound, upper_bound)

    # Salvar métricas num CSV
    if all_metrics:
        save_metrics_to_csv(all_metrics)
        print(f"\n{'='*60}")
        print(f"✓ Métricas salvas em data/metricas_execucao.csv")
        print(f"✓ Total de testes executados: {len(all_metrics)}")
        print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
