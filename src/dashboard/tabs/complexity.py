"""
Tab 5: Complexidade
"""
import streamlit as st
import pandas as pd
from dashboard.config import COMPLEXITY_DATA
from dashboard.charts import create_complexity_verification_chart


def render_complexity_tab(df: pd.DataFrame):
    """
    Renderiza a tab de análise de complexidade

    Args:
        df: DataFrame com os dados
    """
    st.header("📊 Análise de Complexidade (Big O)")

    # Tabela de complexidades
    st.subheader("📋 Tabela Resumo de Complexidades")
    df_complexity = pd.DataFrame(COMPLEXITY_DATA)
    st.dataframe(df_complexity, hide_index=True, use_container_width=True)

    st.markdown("---")

    # Verificação experimental
    st.subheader("🔬 Verificação Experimental de Complexidade")

    st.markdown("""
    **Método:** Analisando a taxa de crescimento das operações em relação ao tamanho do array.

    Para confirmar a complexidade:
    - **O(n):** Operações crescem linearmente
    - **O(n log n):** Operações crescem de forma log-linear
    - **O(n²):** Operações crescem quadraticamente
    """)

    algo_selected = st.selectbox(
        "Selecione um algoritmo para análise:",
        df['algorithm'].unique(),
        format_func=lambda x: x.title()
    )

    fig_complexity = create_complexity_verification_chart(df, algo_selected)
    st.plotly_chart(fig_complexity, use_container_width=True)

    # Análise de fit
    st.info("""
    💡 **Como interpretar:**
    - Se a linha real segue **O(n)**: complexidade linear
    - Se a linha real segue **O(n log n)**: complexidade log-linear
    - Se a linha real segue **O(n²)**: complexidade quadrática
    """)
