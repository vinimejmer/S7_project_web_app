import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Leemmos el csv
car_data = pd.read_csv('vehicles_us.csv')

# Creamos un botón en la aplicación streamlit
build_histogram = st.checkbox('Construir Histograma')
build_scatter = st.checkbox('Construir Gráfico de Dispersión')

# Lógica para ejecutar cuando se hace click en el botón
if build_histogram:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma con plotly
    # Se crea una figura vacía

    fig = go.Figure(data=(go.Histogram(x = car_data['odometer'])))

    # Añadimos un título

    fig.update_layout(title_text = 'Distribución del Odómetro')

    # Mostramos el gráfico plotly en la aplicación streamlit
    # 'use_container_width = True, ajusta el ancho del gráfico al contenedor

    st.plotly_chart(fig, use_container_width=True)

elif build_scatter:
    # Escribimos el mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # creamos el gráfico de dispersión
    fig = go.Figure(data = [go.Scatter(x = car_data['odometer'], y = car_data['price'], mode = 'markers')])

    # agregamos título
    fig.update_layout(title_text = 'Relación entre Odómetro y Precio')

    # Mostramos el gráfico
    st.plotly_chart(fig, use_container_width=True)