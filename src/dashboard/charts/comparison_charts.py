"""
Gráficos relacionados a comparações e trocas
"""
import plotly.express as px
import pandas as pd


def create_comparison_chart(df: pd.DataFrame):
    """
    Cria gráfico de comparações

    Args:
        df: DataFrame com os dados

    Returns:
        Figura plotly
    """
    fig = px.line(
        df[df.array_type == 'random'],
        x='array_size',
        y='comparisons',
        color='algorithm',
        log_x=True,
        log_y=True,
        title="Número de Comparações (Array Aleatório)",
        labels={
            'array_size': 'Tamanho do Array',
            'comparisons': 'Número de Comparações',
            'algorithm': 'Algoritmo'
        }
    )
    fig.update_traces(mode='lines+markers')
    return fig


def create_swaps_chart(df: pd.DataFrame):
    """
    Cria gráfico de trocas

    Args:
        df: DataFrame com os dados

    Returns:
        Figura plotly
    """
    fig = px.line(
        df[df.array_type == 'random'],
        x='array_size',
        y='swaps',
        color='algorithm',
        log_x=True,
        log_y=True,
        title="Número de Trocas (Array Aleatório)",
        labels={
            'array_size': 'Tamanho do Array',
            'swaps': 'Número de Trocas',
            'algorithm': 'Algoritmo'
        }
    )
    fig.update_traces(mode='lines+markers')
    return fig


def create_ratio_chart(df: pd.DataFrame, array_size: int = 10000):
    """
    Cria gráfico de razão entre trocas/comparações

    Args:
        df: DataFrame com os dados
        array_size: Tamanho do array

    Returns:
        Figura plotly
    """
    df_ratio = df[df.array_size == array_size].copy()
    df_ratio['ratio'] = (df_ratio['swaps'] / df_ratio['comparisons'] * 100).fillna(0)

    fig = px.bar(
        df_ratio,
        x='algorithm',
        y='ratio',
        color='array_type',
        barmode='group',
        title=f"Percentual de Trocas em relação às Comparações ({array_size//1000}k elementos)",
        labels={
            'algorithm': 'Algoritmo',
            'ratio': 'Trocas/Comparações (%)',
            'array_type': 'Tipo de Array'
        }
    )

    return fig
