"""
Componente de Sidebar
"""
import streamlit as st
from dashboard.config import SIDEBAR_INFO


def render_sidebar():
    """Renderiza a sidebar com informações do projeto"""
    st.sidebar.header("⚙️ Configurações")
    st.sidebar.markdown(SIDEBAR_INFO)
