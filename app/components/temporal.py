import streamlit as st
import plotly.express as px
import pandas as pd

def show_temporal_analysis(df):
    """
    Mostrar análisis temporal de eventos sísmicos.
    """
    st.markdown("### ⏱️ Análisis Temporal")
    
    # Preparar datos agregados por año y mes
    monthly_stats = df.groupby(['Year', 'Month', 'tsunami']).agg({
        'magnitude': ['mean', 'max', 'count'],
        'depth': 'mean',
        'sig': 'mean'
    }).reset_index()
    
    # Aplanar columnas multinivel
    monthly_stats.columns = [
        'Year', 'Month', 'tsunami', 'magnitude_mean', 'magnitude_max',
        'event_count', 'depth_mean', 'sig_mean'
    ]
    
    # Crear fecha para visualización
    monthly_stats['Date'] = pd.to_datetime(
        monthly_stats[['Year', 'Month']].assign(day=1)
    )
    monthly_stats['tsunami'] = monthly_stats['tsunami'].map({
        0: 'Sin Tsunami',
        1: 'Con Tsunami'
    })
    
    # Gráfico de evolución temporal
    fig = px.bar(
        monthly_stats,
        x='Date',
        y='magnitude_mean',
        color='tsunami',
        title='Evolución de Magnitud Promedio por Año',
        labels={
            'magnitude_mean': 'Magnitud Promedio',
            'Date': 'Fecha'
        }
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Distribución anual de tsunamis
    fig = px.histogram(
        df[df['tsunami'] == 1],
        x='Year',
        title='Distribución Anual de Tsunamis',
        labels={'Year': 'Año', 'count': 'Número de Tsunamis'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Análisis de tendencias
    col1, col2 = st.columns(2)
    
    with col1:
        yearly_events = df.groupby('Year').size().reset_index(name='count')
        fig = px.line(
            yearly_events,
            x='Year',
            y='count',
            title='Tendencia de Eventos Sísmicos por Año'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        yearly_magnitude = df.groupby('Year')['magnitude'].mean().reset_index()
        fig = px.line(
            yearly_magnitude,
            x='Year',
            y='magnitude',
            title='Tendencia de Magnitud Media por Año'
        )
        st.plotly_chart(fig, use_container_width=True)
