"""
Funções para manipulação de arquivos CSV
"""
import csv


def save_metrics_to_csv(metrics_list: list[dict], filename: str = 'data/metricas_execucao.csv'):
    """
    Salva métricas de execução em arquivo CSV

    Args:
        metrics_list: Lista de dicionários com métricas
        filename: Nome do arquivo CSV (default: data/metricas_execucao.csv)
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['algorithm', 'array_type', 'array_size', 'comparisons', 'swaps',
                     'recursive_calls', 'execution_time', 'memory_current', 'memory_peak']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for metric in metrics_list:
            writer.writerow({
                'algorithm': metric.get('algorithm', 'unknown'),
                'array_type': metric.get('array_type', 'random'),
                'array_size': metric['array_size'],
                'comparisons': metric['comparisons'],
                'swaps': metric['swaps'],
                'recursive_calls': metric.get('recursive_calls', 0),
                'execution_time': metric['execution_time'],
                'memory_current': metric['memory_usage'][0],
                'memory_peak': metric['memory_usage'][1]
            })
