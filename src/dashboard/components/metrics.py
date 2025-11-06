"""
Componentes de métricas e cards
"""
import streamlit as st
import pandas as pd


def render_overview_metrics(df: pd.DataFrame):
    """
    Renderiza as métricas da visão geral

    Args:
        df: DataFrame com os dados de execução
    """
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Algoritmos Analisados",
            value="6",
            delta="Bubble, Insertion, Selection, Merge, Quick, Shell"
        )

    with col2:
        st.metric(
            label="Total de Testes",
            value=len(df),
            delta=f"{len(df.algorithm.unique())} algoritmos × {len(df.array_size.unique())} tamanhos × {len(df.array_type.unique())} tipos"
        )

    with col3:
        # Filtrar apenas arrays aleatórios para uma comparação justa
        fastest_random = df[(df.array_size == 10000) & (df.array_type == 'random')].sort_values('execution_time').iloc[0]
        st.metric(
            label="🏆 Mais Rápido (10k, aleatório)",
            value=fastest_random['algorithm'].title(),
            delta=f"{fastest_random['execution_time']:.3f}s"
        )

    with col4:
        # Mostrar o melhor caso absoluto (Insertion Sort em array ordenado)
        fastest_overall = df[df.array_size == 10000].sort_values('execution_time').iloc[0]
        array_type_label = {
            'random': 'aleatório',
            'ordered': 'ordenado',
            'reverse': 'reverso'
        }[fastest_overall['array_type']]

        st.metric(
            label=f"⚡ Melhor Caso Absoluto (10k, {array_type_label})",
            value=fastest_overall['algorithm'].title(),
            delta=f"{fastest_overall['execution_time']:.3f}s"
        )
