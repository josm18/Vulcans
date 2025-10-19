import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def create_global_map(df):
    """
    Crear mapa global de terremotos coloreado por magnitud.
    """
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='magnitude',
        hover_data=['depth', 'tsunami', 'sig', 'dmin'],
        projection='natural earth',
        size='sig',
        title='Distribución Global de Terremotos por Magnitud'
    )
    
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)

def create_tsunami_depth_map(df):
    """
    Crear mapa de tsunamis vs profundidad del epicentro.
    """
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='tsunami',
        size='depth',
        hover_data=['magnitude', 'depth', 'sig', 'Year'],
        color_discrete_map={0: 'lightblue', 1: 'red'},
        title='Tsunamis vs Profundidad del Epicentro'
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def create_risk_zones_map(df):
    """
    Crear mapa de zonas de alto riesgo (Ring of Fire).
    """
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='magnitude',
        size='sig',
        symbol='tsunami',
        hover_data=['depth', 'Year', 'cdi'],
        color_continuous_scale='Viridis',
        symbol_map={0: 'circle', 1: 'diamond'},
        title='Ring of Fire: Zonas de Alto Riesgo'
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
