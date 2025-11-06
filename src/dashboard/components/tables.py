"""
Componentes de tabelas
"""
import pandas as pd


def create_summary_table(df: pd.DataFrame, array_size: int = 10000, array_type: str = 'random') -> pd.DataFrame:
    """
    Cria tabela resumo para um tamanho e tipo específico de array

    Args:
        df: DataFrame com os dados
        array_size: Tamanho do array
        array_type: Tipo do array

    Returns:
        DataFrame formatado com resumo
    """
    df_filtered = df[(df.array_size == array_size) & (df.array_type == array_type)].copy()
    df_filtered = df_filtered.sort_values('execution_time')

    summary_table = df_filtered[[
        'algorithm', 'execution_time', 'comparisons',
        'swaps', 'recursive_calls', 'memory_peak'
    ]].copy()

    summary_table.columns = [
        'Algoritmo', 'Tempo (s)', 'Comparações',
        'Trocas', 'Chamadas Recursivas', 'Memória Pico (bytes)'
    ]

    summary_table['Algoritmo'] = summary_table['Algoritmo'].str.title()
    summary_table['Tempo (s)'] = summary_table['Tempo (s)'].round(3)

    return summary_table


def create_pivot_table(df: pd.DataFrame, values: str, index: list, columns: str) -> pd.DataFrame:
    """
    Cria tabela pivot genérica

    Args:
        df: DataFrame com os dados
        values: Coluna de valores
        index: Colunas de índice
        columns: Coluna de colunas

    Returns:
        DataFrame pivot formatado
    """
    pivot_table = df.pivot_table(
        values=values,
        index=index,
        columns=columns,
        aggfunc='mean'
    ).round(6)

    return pivot_table
