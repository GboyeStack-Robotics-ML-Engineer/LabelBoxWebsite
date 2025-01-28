import streamlit as st
import streamlit.components.v1 as components

# Load the HTML file
with open("Frontend/index.html", "r") as file:
    html_content = file.read()
st.write(html_content)
# Render the HTML file in Streamlit
components.html(html_content, height=800, scrolling=True)
