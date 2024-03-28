import streamlit as st
from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--headless=new')

if "driver" not in st.session_state:
    st.session_state.driver = webdriver.Chrome(options=options)

st.session_state.driver.get('https://www.python.org/')

st.write(st.session_state.driver.title)
print(st.session_state.driver.title)
st.session_state.driver.close()