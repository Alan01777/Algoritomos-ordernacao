"""
Tab 6: Lógica dos Algoritmos
"""
import streamlit as st
from pathlib import Path
from dashboard.content import ALGORITHM_INFO
from dashboard.config import ALGORITHM_ADVANTAGES, ALGORITHM_DISADVANTAGES


def render_logic_tab(df):
    """
    Renderiza a tab de lógica dos algoritmos

    Args:
        df: DataFrame com os dados (não utilizado nesta tab)
    """
    st.header("Lógica e Estratégias dos Algoritmos")

    algo_selected = st.selectbox(
        "Selecione um algoritmo para análise:",
        list(ALGORITHM_INFO.keys())
    )

    info = ALGORITHM_INFO[algo_selected]

    # Cabeçalho do algoritmo
    st.subheader(f"{info.get('emoji', '📚')} {algo_selected}")
    st.markdown(f"**Estratégia:** {info['estrategia']}")

    if 'analogia_principal' in info:
        st.info(f"**Conceito principal:** {info['analogia_principal']}")

    st.markdown(f"**Complexidade computacional:** {info['complexidade']}")

    st.markdown("---")

    # Tabs para organizar conteúdo
    subtab1, subtab2, subtab3, subtab4 = st.tabs([
        "Descrição Conceitual",
        "Exemplo Visual",
        "Código-Fonte",
        "Recomendações de Uso"
    ])

    # Tab 1: Descrição conceitual
    with subtab1:
        st.subheader("Descrição do Algoritmo")

        if 'analogias' in info:
            for idx, analogia in enumerate(info['analogias'], 1):
                with st.expander(f"{analogia['titulo']}", expanded=(idx == 1)):
                    st.markdown(analogia['descricao'])
        else:
            st.markdown(info.get('descricao', 'Descrição não disponível'))

        if 'curiosidade' in info:
            st.success(f"**Nota histórica:** {info['curiosidade']}")

    # Tab 2: Exemplo Visual
    with subtab2:
        if info.get('exemplo_visual'):
            st.markdown("### Execução Passo a Passo")
            st.code(info['exemplo_visual'], language='text')
        else:
            st.info("Exemplo de execução não disponível para este algoritmo.")

    # Tab 3: Código-Fonte
    with subtab3:
        st.subheader("Implementação em Python")

        # Determinar caminho base (src/algorithms/)
        current_file = Path(__file__)
        src_dir = current_file.parent.parent.parent
        algorithms_dir = src_dir / "algorithms"

        file_map = {
            "Bubble Sort": "bubblesort.py",
            "Insertion Sort": "insertionsort.py",
            "Selection Sort": "selectionsort.py",
            "Merge Sort": "mergesort.py",
            "Quick Sort": "quicksort.py",
            "Shell Sort": "shellsort.py"
        }

        try:
            file_path = algorithms_dir / file_map[algo_selected]
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()

            st.code(code, language='python')
        except FileNotFoundError:
            st.error(f"Arquivo de implementação não encontrado: {file_path}")
        except Exception as e:
            st.error(f"Erro ao ler arquivo: {str(e)}")

    # Tab 4: Quando Usar
    with subtab4:
        st.subheader("Contextos de Aplicação")
        st.markdown(f"**{info['quando_usar']}**")

        st.markdown("---")

        # Vantagens e desvantagens
        col1, col2 = st.columns(2)

        with col1:
            st.success("**Vantagens**")
            for adv in ALGORITHM_ADVANTAGES.get(algo_selected, []):
                st.markdown(f"- {adv}")

        with col2:
            st.error("**Desvantagens**")
            for dis in ALGORITHM_DISADVANTAGES.get(algo_selected, []):
                st.markdown(f"- {dis}")
