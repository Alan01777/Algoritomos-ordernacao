"""
Tab 4: Chamadas Recursivas
"""
import streamlit as st
import pandas as pd
from dashboard.charts import create_recursive_line_chart, create_depth_chart
from dashboard.components import create_pivot_table


def render_recursion_tab(df: pd.DataFrame):
    """
    Renderiza a tab de chamadas recursivas

    Args:
        df: DataFrame com os dados
    """
    st.header("🔄 Análise de Chamadas Recursivas")

    st.info("""
    📌 **Algoritmos Recursivos:** Merge Sort e Quick Sort
    📌 **Algoritmos Iterativos:** Bubble Sort, Insertion Sort, Selection Sort, Shell Sort
    """)

    # Filtrar apenas algoritmos recursivos
    df_recursive = df[df.recursive_calls > 0].copy()

    if len(df_recursive) == 0:
        st.warning("⚠️ Nenhum dado de chamadas recursivas encontrado.")
    else:
        # Gráfico de chamadas recursivas vs tamanho
        st.subheader("📈 Chamadas Recursivas vs Tamanho do Array")
        fig_rec = create_recursive_line_chart(df_recursive)
        st.plotly_chart(fig_rec, use_container_width=True)

        st.markdown("---")

        # Comparação teórica vs prática
        st.subheader("📊 Comparação: Teórico vs Prático")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            ### Merge Sort
            **Teórico:** ~n chamadas recursivas
            - Divide sempre ao meio
            - Árvore binária completa
            - Profundidade: O(log n)

            **Exemplo para n=10:**
            - Esperado: ~10 chamadas
            """)

        with col2:
            st.markdown("""
            ### Quick Sort (Otimizado)
            **Teórico:** O(log n) a O(n) chamadas
            - Depende do balanceamento das partições
            - Otimizações reduzem chamadas
            - Profundidade: O(log n) com tail call optimization

            **Exemplo para n=10:**
            - Esperado: ~6-10 chamadas (depende do pivô)
            """)

        # Tabela comparativa
        st.subheader("📋 Tabela de Chamadas Recursivas")
        pivot_rec = create_pivot_table(
            df_recursive,
            values='recursive_calls',
            index=['algorithm', 'array_size'],
            columns='array_type'
        )
        pivot_rec = pivot_rec.round(0)
        st.dataframe(pivot_rec, use_container_width=True)

        # Análise de profundidade
        st.subheader("🌳 Profundidade Estimada da Recursão")
        fig_depth = create_depth_chart(df_recursive)
        st.plotly_chart(fig_depth, use_container_width=True)
