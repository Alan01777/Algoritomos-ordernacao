"""
Gráficos relacionados a chamadas recursivas
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def create_recursive_line_chart(df: pd.DataFrame):
    """
    Cria gráfico de linha de chamadas recursivas

    Args:
        df: DataFrame com os dados

    Returns:
        Figura plotly
    """
    fig = px.line(
        df,
        x='array_size',
        y='recursive_calls',
        color='algorithm',
        facet_col='array_type',
        log_x=True,
        log_y=True,
        title="Número de Chamadas Recursivas",
        labels={
            'array_size': 'Tamanho do Array (n)',
            'recursive_calls': 'Número de Chamadas Recursivas',
            'algorithm': 'Algoritmo',
            'array_type': 'Tipo de Array'
        }
    )

    fig.update_traces(mode='lines+markers')
    return fig


def create_depth_chart(df: pd.DataFrame):
    """
    Cria gráfico de profundidade da recursão

    Args:
        df: DataFrame com os dados (apenas array_type == 'random')

    Returns:
        Figura plotly
    """
    df_depth = df[df.array_type == 'random'].copy()
    df_depth['expected_depth'] = np.log2(df_depth['array_size'])

    fig = go.Figure()

    for algo in df_depth['algorithm'].unique():
        algo_data = df_depth[df_depth['algorithm'] == algo]

        fig.add_trace(go.Scatter(
            x=algo_data['array_size'],
            y=np.log2(algo_data['recursive_calls']),
            mode='lines+markers',
            name=f"{algo.title()} (real)"
        ))

    # Linha teórica log(n)
    fig.add_trace(go.Scatter(
        x=df_depth['array_size'].unique(),
        y=np.log2(df_depth['array_size'].unique()),
        mode='lines',
        name='Teórico: O(log n)',
        line=dict(dash='dash', color='gray')
    ))

    fig.update_layout(
        title="Profundidade da Recursão: log₂(chamadas recursivas)",
        xaxis_title="Tamanho do Array (n)",
        yaxis_title="log₂(Chamadas Recursivas)",
        xaxis_type="log",
        height=400
    )

    return fig
