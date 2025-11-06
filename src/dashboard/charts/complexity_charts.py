"""
Gráficos relacionados à análise de complexidade
"""
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def create_radar_chart(df: pd.DataFrame):
    """
    Cria gráfico de radar comparativo

    Args:
        df: DataFrame com os dados (10k elementos, aleatório)

    Returns:
        Figura plotly
    """
    df_radar = df.copy()

    # Inverter tempo (menor é melhor) e normalizar
    df_radar['speed'] = 100 * (1 - (df_radar['execution_time'] - df_radar['execution_time'].min()) /
                                (df_radar['execution_time'].max() - df_radar['execution_time'].min()))

    # Inverter comparações (menor é melhor) e normalizar
    df_radar['efficiency'] = 100 * (1 - (df_radar['comparisons'] - df_radar['comparisons'].min()) /
                                    (df_radar['comparisons'].max() - df_radar['comparisons'].min()))

    # Inverter memória (menor é melhor) e normalizar
    df_radar['memory_eff'] = 100 * (1 - (df_radar['memory_peak'] - df_radar['memory_peak'].min()) /
                                    (df_radar['memory_peak'].max() - df_radar['memory_peak'].min()))

    fig = go.Figure()

    for algo in df_radar['algorithm'].unique():
        algo_data = df_radar[df_radar['algorithm'] == algo].iloc[0]

        fig.add_trace(go.Scatterpolar(
            r=[algo_data['speed'], algo_data['efficiency'], algo_data['memory_eff']],
            theta=['Velocidade', 'Eficiência<br>(comparações)', 'Memória'],
            fill='toself',
            name=algo.title()
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=True,
        height=500
    )

    return fig


def create_complexity_verification_chart(df: pd.DataFrame, algorithm: str):
    """
    Cria gráfico de verificação de complexidade para um algoritmo

    Args:
        df: DataFrame com os dados
        algorithm: Nome do algoritmo

    Returns:
        Figura plotly
    """
    df_algo = df[(df.algorithm == algorithm) & (df.array_type == 'random')].copy()

    # Calcular taxa de crescimento
    df_algo = df_algo.sort_values('array_size')
    df_algo['n'] = df_algo['array_size']
    df_algo['n_log_n'] = df_algo['array_size'] * np.log2(df_algo['array_size'])
    df_algo['n_squared'] = df_algo['array_size'] ** 2

    # Normalizar
    df_algo['comp_norm'] = df_algo['comparisons'] / df_algo['comparisons'].iloc[0]
    df_algo['n_norm'] = df_algo['n'] / df_algo['n'].iloc[0]
    df_algo['n_log_n_norm'] = df_algo['n_log_n'] / df_algo['n_log_n'].iloc[0]
    df_algo['n_squared_norm'] = df_algo['n_squared'] / df_algo['n_squared'].iloc[0]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_algo['array_size'],
        y=df_algo['comp_norm'],
        mode='lines+markers',
        name='Comparações (real)',
        line=dict(width=3)
    ))

    fig.add_trace(go.Scatter(
        x=df_algo['array_size'],
        y=df_algo['n_norm'],
        mode='lines',
        name='O(n)',
        line=dict(dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=df_algo['array_size'],
        y=df_algo['n_log_n_norm'],
        mode='lines',
        name='O(n log n)',
        line=dict(dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=df_algo['array_size'],
        y=df_algo['n_squared_norm'],
        mode='lines',
        name='O(n²)',
        line=dict(dash='dash')
    ))

    fig.update_layout(
        title=f"Verificação de Complexidade - {algorithm.title()}",
        xaxis_title="Tamanho do Array (n)",
        yaxis_title="Taxa de Crescimento (normalizada)",
        xaxis_type="log",
        yaxis_type="log",
        height=500
    )

    return fig
