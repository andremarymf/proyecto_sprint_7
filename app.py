
import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis de datos de vehículos')
# Leer los datos
car_data = pd.read_csv(r'C:\Users\Mariana Montoya\OneDrive - Winncom Techologies Corp\Desktop\proyecto_7\vehicles_us.csv') # leer los datos

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter_plot = st.checkbox('Mostrar gráfico de dispersión')
if build_scatter_plot:
    st.write('gráfico de dispersión para datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)