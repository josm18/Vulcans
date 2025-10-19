import streamlit as st

def apply_custom_style():
    """
    Aplicar estilos personalizados a la aplicación Streamlit.
    """
    st.markdown("""
    <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Estilo para títulos */
        h1 {
            color: #2E86C1;
            font-weight: 600;
        }
        
        h2, h3 {
            color: #2874A6;
            margin-top: 2rem;
        }
        
        /* Estilo para métricas */
        .metric-container {
            background-color: #F8F9F9;
            border-radius: 5px;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Estilo para gráficos */
        .plot-container {
            background-color: white;
            border-radius: 5px;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 1rem 0;
        }
        
        /* Estilo para sidebar */
        .sidebar .sidebar-content {
            background-color: #F8F9F9;
        }
        
        /* Estilo para tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 4rem;
            white-space: pre-wrap;
            background-color: #F8F9F9;
            border-radius: 4px 4px 0 0;
            gap: 1rem;
            padding: 1rem 2rem;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #2E86C1;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)
