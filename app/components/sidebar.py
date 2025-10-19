import streamlit as st
import pandas as pd

def sidebar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crear y manejar el sidebar con filtros interactivos.
    
    Args:
        df (pd.DataFrame): DataFrame original
        
    Returns:
        pd.DataFrame: DataFrame filtrado según las selecciones del usuario
    """
    st.sidebar.title("🎯 Filtros de Análisis")
    
    # Filtro de años
    year_range = st.sidebar.slider(
        "Rango de Años",
        min_value=int(df['Year'].min()),
        max_value=int(df['Year'].max()),
        value=(int(df['Year'].min()), int(df['Year'].max()))
    )
    
    # Filtro de magnitud
    magnitude_range = st.sidebar.slider(
        "Rango de Magnitud",
        min_value=float(df['magnitude'].min()),
        max_value=float(df['magnitude'].max()),
        value=(float(df['magnitude'].min()), float(df['magnitude'].max()))
    )
    
    # Filtro de profundidad
    depth_range = st.sidebar.slider(
        "Rango de Profundidad (km)",
        min_value=float(df['depth'].min()),
        max_value=float(df['depth'].max()),
        value=(float(df['depth'].min()), float(df['depth'].max()))
    )
    
    # Filtro de tsunamis
    tsunami_filter = st.sidebar.multiselect(
        "Filtrar por Tsunami",
        options=[0, 1],
        default=[0, 1],
        format_func=lambda x: "Con Tsunami" if x == 1 else "Sin Tsunami"
    )
    
    # Aplicar filtros
    filtered_df = df[
        (df['Year'].between(year_range[0], year_range[1])) &
        (df['magnitude'].between(magnitude_range[0], magnitude_range[1])) &
        (df['depth'].between(depth_range[0], depth_range[1])) &
        (df['tsunami'].isin(tsunami_filter))
    ]
    
    # Información sobre los filtros aplicados
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Resumen de Filtros")
    st.sidebar.markdown(f"**Eventos mostrados:** {len(filtered_df)}")
    st.sidebar.markdown(f"**Tsunamis:** {filtered_df['tsunami'].sum()}")
    
    return filtered_df
