import streamlit as st

st.title("Graus celsius para fahrenheit")
num1 = st.number_input("digite o valor em celsius")
if st.button("calcular em fahrenheit"):
    result1 = (num1 * 9/5) + 32
    st.text(f"O resultado em Fahrenheit é {result1}")
    st.title("Obrigado!")
if st.button("calcular em kelvin"):
    result1 = num1 + 273.15
    st.text(f"O resultado em Kelvin é {result1}")
    st.title("Obrigado!")
