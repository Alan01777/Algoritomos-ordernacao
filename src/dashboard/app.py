"""
Aplicação Streamlit - Análise de Algoritmos de Ordenação
Atividade Acadêmica - Complexidade de Algoritmos

Arquivo principal refatorado - apenas orquestração
"""

import sys
from pathlib import Path

# Adicionar o diretório src ao PYTHONPATH se necessário
current_dir = Path(__file__).parent
src_dir = current_dir.parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

import streamlit as st

# Importações dos módulos
from dashboard.config import PAGE_CONFIG
from dashboard.components import render_sidebar
from dashboard.data import load_data
from dashboard.tabs import (
    render_overview_tab,
    render_execution_time_tab,
    render_comparisons_tab,
    render_recursion_tab,
    render_complexity_tab,
    render_logic_tab,
    render_conclusions_tab
)

# Configuração da página
st.set_page_config(**PAGE_CONFIG)

# Título principal
st.title("Análise Comparativa de Algoritmos de Ordenação")
st.markdown("""
*Estudo experimental sobre complexidade computacional e desempenho de algoritmos de ordenação*
""")
st.markdown("---")

# Sidebar
render_sidebar()

# Carregar dados
df = load_data()

# Tabs principais
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Visão Geral",
    "Tempo de Execução",
    "Comparações e Trocas",
    "Chamadas Recursivas",
    "Complexidade",
    "Lógica dos Algoritmos",
    "Conclusões"
])

# Renderizar cada tab
with tab1:
    render_overview_tab(df)

with tab2:
    render_execution_time_tab(df)

with tab3:
    render_comparisons_tab(df)

with tab4:
    render_recursion_tab(df)

with tab5:
    render_complexity_tab(df)

with tab6:
    render_logic_tab(df)

with tab7:
    render_conclusions_tab(df)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p style='color: #666; font-size: 0.9em;'>
        Análise de Algoritmos de Ordenação<br>
        Desenvolvido com Streamlit e Plotly
    </p>
</div>
""", unsafe_allow_html=True)
