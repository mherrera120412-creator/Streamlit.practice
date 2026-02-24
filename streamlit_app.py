import streamlit as st

st.title("Mi primera app en Streamlit 🚀")

st.write("Hola, esta es mi primera aplicación desplegada en Streamlit Cloud.")

numero = st.number_input("Escribe un número:")

st.write("El doble es:", numero * 2)
