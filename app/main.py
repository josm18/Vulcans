import streamlit as st
import pandas as pd
import plotly.express as px
from components.sidebar import sidebar
from components.maps import create_global_map, create_tsunami_depth_map, create_risk_zones_map
from components.analytics import show_correlation_analysis, show_multivariate_analysis
from components.temporal import show_temporal_analysis
from utils.data_loader import load_data
from utils.styling import apply_custom_style

def main():
    # Configuración inicial de la página
    st.set_page_config(
        page_title="Análisis Global de Terremotos y Tsunamis",
        page_icon="🌊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Aplicar estilos personalizados
    apply_custom_style()
    
    # Cargar datos
    df = load_data()
    
    # Crear sidebar con filtros
    filtered_df = sidebar(df)
    
    # Header principal
    st.title("🌊 Dashboard de Análisis Sísmico y Tsunamis")
    st.markdown("### Sistema de Monitoreo y Análisis de Eventos Sísmicos Globales")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Eventos", len(filtered_df))
    with col2:
        st.metric("Tsunamis Generados", filtered_df['tsunami'].sum())
    with col3:
        st.metric("Magnitud Máxima", filtered_df['magnitude'].max())
    with col4:
        st.metric("Profundidad Media", f"{filtered_df['depth'].mean():.2f} km")
    
    # Tabs para diferentes secciones
    tab1, tab2, tab3, tab4 = st.tabs([
        "🗺️ Análisis Geoespacial",
        "📊 Análisis de Correlaciones",
        "📈 Análisis Multivariable",
        "⏱️ Análisis Temporal"
    ])
    
    with tab1:
        st.markdown("### Distribución Global de Eventos Sísmicos")
        create_global_map(filtered_df)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Tsunamis vs Profundidad")
            create_tsunami_depth_map(filtered_df)
        with col2:
            st.markdown("### Zonas de Alto Riesgo")
            create_risk_zones_map(filtered_df)
    
    with tab2:
        show_correlation_analysis(filtered_df)
    
    with tab3:
        show_multivariate_analysis(filtered_df)
    
    with tab4:
        show_temporal_analysis(filtered_df)

if __name__ == "__main__":
    main()
