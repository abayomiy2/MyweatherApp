
import requests
import streamlit as st
try:
    # imagesize = 300
    # st.title("App with Image")
    # # st.image("images.jpeg")
    # img1 = st.image("image1.jpg", width=imagesize, caption="A man with a sun-shade smiling...")
    # img2 = st.image("image1.jpg", width=imagesize, caption="A man with a sun-shade smiling...")
    # img3 = st.image("image1.jpg", width=imagesize, caption="A man with a sun-shade smiling...")
    # all_images = [img1, img2, img3]
    # for img in all_images:
    #     st.image()

    # Declare your columns
    # col1, col2 = st.columns(2, gap="large", vertical_alignment="bottom")
    #
    # with col1:
    #     st.image("city.jpg")
    #
    # with col2:
    #     st.header("Sign up")
    #     st.write("Register for our City guide")
    #     st.text_input("", placeholder="Full Name")
    #     st.text_input("", placeholder="Email Address")
    #     st.text_area("", placeholder="Type your message here...")

    image_size=300
    st.title('Weather App')
    st.image("weather image.jpg ",width= image_size)
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
