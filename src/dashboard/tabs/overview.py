"""
Tab 1: Visão Geral
"""
import streamlit as st
import pandas as pd
from dashboard.components import render_overview_metrics, create_summary_table
from dashboard.charts import create_radar_chart


def render_overview_tab(df: pd.DataFrame):
    """
    Renderiza a tab de visão geral

    Args:
        df: DataFrame com os dados
    """
    st.header("Visão Geral dos Resultados")

    # Métricas
    render_overview_metrics(df)

    # Nota explicativa
    st.info("""
    **Nota sobre as métricas apresentadas:**
    - **Mais rápido (dados aleatórios):** Algoritmo com melhor desempenho para dados aleatórios, representando o caso médio mais comum
    - **Melhor caso absoluto:** Combinação de algoritmo e tipo de entrada que resulta no menor tempo de execução (tipicamente Insertion Sort em dados pré-ordenados)
    """)

    st.markdown("---")

    # Tabela resumo
    st.subheader("Tabela Resumo: Arranjo de 10.000 elementos (Aleatório)")
    summary_table = create_summary_table(df, array_size=10000, array_type='random')
    st.dataframe(summary_table, hide_index=True, use_container_width=True)

    st.markdown("---")

    # Gráfico de radar comparativo
    st.subheader("Comparação Multidimensional (10.000 elementos, aleatório)")
    df_10k = df[(df.array_size == 10000) & (df.array_type == 'random')].copy()
    fig_radar = create_radar_chart(df_10k)
    st.plotly_chart(fig_radar, use_container_width=True)
