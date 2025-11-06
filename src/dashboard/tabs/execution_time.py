"""
Tab 2: Tempo de Execução
"""
import streamlit as st
import pandas as pd
from dashboard.charts import create_time_line_chart, create_time_bar_chart
from dashboard.components import create_pivot_table


def render_execution_time_tab(df: pd.DataFrame):
    """
    Renderiza a tab de tempo de execução

    Args:
        df: DataFrame com os dados
    """
    st.header("⏱️ Análise de Tempo de Execução")

    # Seletor de tipo de array
    array_type_filter = st.selectbox(
        "Selecione o tipo de array:",
        ["Todos", "random", "ordered", "reverse"],
        format_func=lambda x: {
            "Todos": "Todos os tipos",
            "random": "Aleatório",
            "ordered": "Ordenado",
            "reverse": "Reverso"
        }[x]
    )

    # Filtrar dados
    if array_type_filter != "Todos":
        df_time = df[df.array_type == array_type_filter]
    else:
        df_time = df.copy()

    # Gráfico de linha - Tempo vs Tamanho
    st.subheader("📈 Tempo de Execução vs Tamanho do Array")
    fig_time = create_time_line_chart(df, array_type_filter)
    st.plotly_chart(fig_time, use_container_width=True)

    # Gráfico de barras - Comparação por tamanho
    st.subheader("📊 Comparação de Tempo por Tamanho")

    size_selected = st.select_slider(
        "Selecione o tamanho do array:",
        options=[10, 100, 1000, 10000]
    )

    fig_bar = create_time_bar_chart(df_time, size_selected)
    st.plotly_chart(fig_bar, use_container_width=True)

    # Tabela detalhada
    st.subheader("📋 Tabela Detalhada de Tempos")
    pivot_table = create_pivot_table(
        df_time,
        values='execution_time',
        index=['algorithm', 'array_size'],
        columns='array_type'
    )
    st.dataframe(pivot_table, use_container_width=True)
