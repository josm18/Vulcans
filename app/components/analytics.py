import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_correlation_analysis(df):
    """
    Mostrar análisis de correlaciones.
    """
    st.markdown("### 📊 Matriz de Correlaciones")
    
    # Calcular correlaciones
    cols = df.select_dtypes(['float64', 'int64']).columns
    corr = df[cols].corr(method='spearman')
    
    # Crear heatmap con plotly
    fig = px.imshow(
        corr,
        labels=dict(color="Correlación"),
        x=corr.columns,
        y=corr.columns,
        color_continuous_scale="RdBu"
    )
    
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla de correlaciones significativas
    st.markdown("#### 🎯 Correlaciones Significativas")
    
    correlations = []
    for col1 in corr.columns:
        for col2 in corr.columns:
            if col1 < col2:  # Evitar duplicados
                correlations.append({
                    'Variable 1': col1,
                    'Variable 2': col2,
                    'Correlación': corr.loc[col1, col2]
                })
    
    # Ordenar por valor absoluto de correlación
    correlations = sorted(
        correlations,
        key=lambda x: abs(x['Correlación']),
        reverse=True
    )[:10]  # Top 10
    
    # Mostrar tabla
    st.table(pd.DataFrame(correlations).style.format({'Correlación': '{:.2f}'}))

def show_multivariate_analysis(df):
    """
    Mostrar análisis multivariable.
    """
    st.markdown("### 📈 Análisis Multivariable")
    
    # Gráfico 3D
    fig = px.scatter_3d(
        df,
        x='magnitude',
        y='depth',
        z='sig',
        color='tsunami',
        size='sig',
        hover_data=['latitude', 'longitude', 'Year'],
        title='Relación entre Magnitud, Profundidad y Significancia'
    )
    
    fig.update_layout(height=700)
    st.plotly_chart(fig, use_container_width=True)
    
    # Distribución de magnitudes
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.box(
            df,
            x='tsunami',
            y='magnitude',
            color='tsunami',
            title='Distribución de Magnitudes por Tsunami'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.histogram(
            df,
            x='magnitude',
            color='tsunami',
            barmode='overlay',
            title='Histograma de Magnitudes por Tsunami'
        )
        st.plotly_chart(fig, use_container_width=True)
