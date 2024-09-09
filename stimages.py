
import requests
import streamlit as st
try:
    st.title('Weather App')
    st.header('check your daily weather info here:')
    user_location = st.text_input("",placeholder= 'Enter your Country, city and province/state')
    weatherLink = f'http://api.weatherapi.com/v1/current.json?key=e09fb8315197455dac1115933231611&q={user_location}&aqi=yes'
    api = requests.get(weatherLink).json()
    Temperature= api['current']['temp_c']
    Weather_Condition = api['current']['condition']['text']
    Humidity= api['current']['humidity']
    st.info(f'''WEATHER FORECAST\n
    TEMPERATURE: {Temperature}_C\n
    WEATHER CONDITION: {Weather_Condition}\n
    HUMIDITY: {Humidity}
    ''')
except KeyError:
    st.warning("")
