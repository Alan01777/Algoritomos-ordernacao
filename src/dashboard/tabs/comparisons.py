"""
Tab 3: Comparações e Trocas
"""
import streamlit as st
import pandas as pd
from dashboard.charts import create_comparison_chart, create_swaps_chart, create_ratio_chart


def render_comparisons_tab(df: pd.DataFrame):
    """
    Renderiza a tab de comparações e trocas

    Args:
        df: DataFrame com os dados
    """
    st.header("🔢 Análise de Comparações e Trocas")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Comparações")
        fig_comp = create_comparison_chart(df)
        st.plotly_chart(fig_comp, use_container_width=True)

    with col2:
        st.subheader("🔄 Trocas")
        fig_swaps = create_swaps_chart(df)
        st.plotly_chart(fig_swaps, use_container_width=True)

    st.markdown("---")

    # Razão Trocas/Comparações
    st.subheader("⚖️ Eficiência: Razão Trocas/Comparações")
    fig_ratio = create_ratio_chart(df, array_size=10000)
    st.plotly_chart(fig_ratio, use_container_width=True)

    st.info("""
    💡 **Interpretação:**
    - **Baixa razão (<5%):** Algoritmo faz muitas comparações mas poucas trocas (ex: Selection Sort)
    - **Alta razão (~100%):** Algoritmo faz troca em quase toda comparação (ex: Insertion Sort em pior caso)
    - **Razão moderada (40-60%):** Equilíbrio entre comparações e trocas (ex: Quick Sort, Merge Sort)
    """)
