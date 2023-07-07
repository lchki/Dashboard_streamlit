import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Définir le style CSS
st.markdown("""
<style>
.container {
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    text-align: center;
}

.container.title h2 {
    border: 2px solid #f5f5f5;
    border-radius: 10px;
    padding: 10px;
    margin: 0;
    color: #333333;
    background-color: #f5f5f5;
}

.container p {
    color: #666666;
    font-size: 18px;
    margin-top: 5px;
    margin-bottom: 5px;
}

.container.title {
    background-color: #f5f5f5;
    color: #333333;
    padding: 20px;
}

.container.heatmap {
    background-color: #f9f9f9;
    margin-bottom: 20px;
}

.container.donut {
    background-color: #fafafa;
    margin-top: 20px;
    padding-top: 20px;
    padding-bottom: 20px;
    border-top: 1px solid #e0e0e0;
    border-bottom: 1px solid #e0e0e0;
}

.container.line {
    background-color: #f5f5f5;
}

.container.line .stLineChart {
    margin-top: 20px;
}

body {
    background-color: #f2f2f2;
    color: #333333;
}

.sidebar-closed .block-container {
    margin-left: 2rem;
    margin-right: 2rem;
}


/* Styles pour les titres des graphiques */
.container.title h2 {
    border: 2px solid #f5f5f5;
    border-radius: 10px;
    padding: 10px;
    margin: 0;
    color: #333333;
    background-color: #f5f5f5;
}background-color: #36b9cc;
}

/* Styles pour les graphiques en mode large */
.wide-mode .stBlock {
    width: 100%;
    padding-left: 0;
    padding-right: 0;
}

</style>
""", unsafe_allow_html=True)

#---- SIDEBAR -----

st.sidebar.header('Dashboard Weather')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max'))

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created by Lucas with help and guidance from Data Professor
''')

#------- ROW A ------
st.markdown('<div class="container title"><h2>Metrics</h2></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.markdown('<div class="container"><h2>Temperature</h2><p>70 °F</p><p>1.2 °F</p></div>', unsafe_allow_html=True)
col2.markdown('<div class="container"><h2>Wind</h2><p>9 mph</p><p>-8%</p></div>', unsafe_allow_html=True)
col3.markdown('<div class="container"><h2>Humidity</h2><p>86%</p><p>4%</p></div>', unsafe_allow_html=True)

st.markdown("---")

#-------- ROW B -------
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

st.markdown("---")
#------- Exclure les colonnes non numériques ------
numeric_columns = seattle_weather.select_dtypes(include=[float, int]).columns
seattle_weather_numeric = seattle_weather[numeric_columns]

st.markdown('<div class="container heatmap"><h2>Heatmap</h2></div>', unsafe_allow_html=True)
fig = px.imshow(seattle_weather_numeric.corr(), color_continuous_scale='viridis')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.markdown('<div class="container donut"><h2>Donut chart</h2></div>', unsafe_allow_html=True)
fig = go.Figure(data=[go.Pie(labels=stocks['company'], values=stocks[donut_theta])])
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

#-------- ROW C -------
st.markdown('<div class="container line"><h2>Line chart</h2></div>', unsafe_allow_html=True)
st.line_chart(seattle_weather, x='date', y=plot_data, height=plot_height)
