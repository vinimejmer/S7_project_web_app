import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Título para la página
st.header('Graficación de Base de datos de autos en venta en US')

# Leemmos el csv
car_data = pd.read_csv('vehicles_us.csv')
car_data_df = pd.DataFrame(car_data)

# Creamos un botón en la aplicación streamlit
build_histogram = st.checkbox('Construir Histograma: Distribución de autos en venta según su kilometraje')
build_scatter = st.checkbox('Construir Gráfico de Dispersión: Relación de precio y kilometraje del auto en venta')

# El dataframe con el que estamos trabajando es el siguiente:
st.write('El dataframe con el que estamos trabajando es el siguiente:')
st.dataframe(car_data_df)

# Cuál es el estado según el tipo de carro
st.subheader('En qué estado se encuentran los coches en venta')
fig = px.sunburst(car_data, path = ['condition','type'])
st.plotly_chart(fig, use_container_width=True)

# Lógica para ejecutar cuando se hace click en el botón
if build_histogram:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para los coches a la venta, según su kilometraje')

    # Crear un histograma con plotly
    # Se crea una figura vacía

    fig = go.Figure(data=(go.Histogram(x = car_data['odometer'])))

    # Añadimos un título

    fig.update_layout(title_text = 'Distribución del Odómetro')

    # Mostramos el gráfico plotly en la aplicación streamlit
    # 'use_container_width = True, ajusta el ancho del gráfico al contenedor

    st.plotly_chart(fig, use_container_width=True)

    # Breve análisis del gráfico
    st.write('El gráfico nos muestra cómo se distribuyen los autos disponibles en venta, según el kilometraje que tienen' \
        'es evidente que, el grueso de los autos en venta se mantienen en kilometrajes bajos-intermedios debajo de las 300k millas' \
        'aunque también hay autos de elevado kilometraje en venta')

elif build_scatter:
    # Escribimos el mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # creamos el gráfico de dispersión
    fig = go.Figure(data = [go.Scatter(x = car_data['odometer'], y = car_data['price'], mode = 'markers')])

    # agregamos título
    fig.update_layout(title_text = 'Relación entre Odómetro y Precio')

    # Mostramos el gráfico
    st.plotly_chart(fig, use_container_width=True)

    # Breve descripción del gráfico
    st.write('Observamos una relación negativa entre el kilometraje en el odómetro y el precio de un auto a la venta' \
    'Esto es porque a mayor kilometraje, los autos han sufrido más desgaste, más reparaciones, y probablemente ya no' \
    'trabajen tan eficientemente. Por ello su precio tiende a disminuir')

    # Hacemos un segundo gráfico que evaluará el impacto del kilometraje, en el tiempo que toma vender un auto

    fig_1 = go.Figure(data = [go.Scatter(x = car_data['odometer'], y = car_data['days_listed'], mode = 'markers')])

    fig_1.update_layout(title_text = 'Relación entre Odómetro y días listado a la venta')

    st.plotly_chart(fig_1, use_container_width=True)

    st.write('Es apreciable en este gráfico una relación esperada. Entre más kilómetros haya recorrido un carro' \
    'más difícil es venderlo, es por eso que se observa que los autos de mayor kiloometraje' \
    'tienen más días listados a la venta')
