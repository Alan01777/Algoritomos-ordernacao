"""
Gráficos relacionados ao tempo de execução
"""
import plotly.express as px
import pandas as pd


def create_time_line_chart(df: pd.DataFrame, array_type_filter: str = "Todos"):
    """
    Cria gráfico de linha de tempo de execução vs tamanho do array

    Args:
        df: DataFrame com os dados
        array_type_filter: Filtro de tipo de array

    Returns:
        Figura plotly
    """
    if array_type_filter != "Todos":
        df_time = df[df.array_type == array_type_filter]
    else:
        df_time = df.copy()

    fig = px.line(
        df_time,
        x='array_size',
        y='execution_time',
        color='algorithm',
        facet_col='array_type' if array_type_filter == "Todos" else None,
        log_x=True,
        log_y=True,
        title="Tempo de Execução (escala log-log)",
        labels={
            'array_size': 'Tamanho do Array',
            'execution_time': 'Tempo (segundos)',
            'algorithm': 'Algoritmo',
            'array_type': 'Tipo de Array'
        }
    )

    fig.update_traces(mode='lines+markers')
    fig.update_layout(height=500)

    return fig


def create_time_bar_chart(df: pd.DataFrame, size_selected: int):
    """
    Cria gráfico de barras de tempo por algoritmo

    Args:
        df: DataFrame com os dados
        size_selected: Tamanho do array selecionado

    Returns:
        Figura plotly
    """
    df_size = df[df.array_size == size_selected]

    fig = px.bar(
        df_size,
        x='algorithm',
        y='execution_time',
        color='array_type',
        barmode='group',
        title=f"Tempo de Execução - Array com {size_selected:,} elementos",
        labels={
            'algorithm': 'Algoritmo',
            'execution_time': 'Tempo (segundos)',
            'array_type': 'Tipo de Array'
        }
    )

    fig.update_layout(height=400)
    return fig
