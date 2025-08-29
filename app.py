"""
Aplicación en python del proyecto irrigation_machine_project
"""

import streamlit as st
import pandas as pd
import plotly.express as px

irrigation_data = pd.read_csv('irrigation_machine.csv') #Leer los datos

st.header('This dataset contains numerical readings from multiple sensors installed in an irrigation machine.')
hist_button = st.button('Build histogram') # Crear un botón
scatter_button = st.button('Build scatter plot')

if hist_button:
    st.write('Creating a histogram for the data set, it will take only 4 sensors to compare')

    fig_h = px.histogram(irrigation_data, x=['sensor_0', 'sensor_6', 'sensor_13', 'sensor_19'], opacity=0.6)

    st.plotly_chart(fig_h, use_container_width=True)

if scatter_button:
    st.write('Creating a scatter plot for the data set, it will take only 4 sensor to compare')

    fig_s = px.scatter(irrigation_data, x=['sensor_0', 'sensor_6', 'sensor_13', 'sensor_19'], opacity=0.6)

    st.plotly_chart(fig_s, use_container_width=True)

