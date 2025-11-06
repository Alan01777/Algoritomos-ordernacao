"""
Carregamento e cache de dados
"""
import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    """Carrega os dados das métricas de execução"""
    try:
        df = pd.read_csv('data/metricas_execucao.csv')
        return df
    except FileNotFoundError:
        st.error("❌ Arquivo 'data/metricas_execucao.csv' não encontrado!")
        st.info("Execute primeiro o script src/main.py para gerar os dados.")
        st.stop()
