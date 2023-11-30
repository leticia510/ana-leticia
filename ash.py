import streamlit as st

st.title("Calculadora")
num1 = st.number_input("digite o primeiro número")
num2 = st.number_input("digite o segundo número")

if st.button("calcular"):
    result1 = num1 + num2
    st.text(f"O resultado da soma entre eles é {result1}")
    result2 = num1 / num2
    st.text(f"O resultado da divisão entre eles é {result2}")
    result3 = num1 * num2
    st.text(f"O resultado da multiplicação entre eles é {result3}")
    result4 = num1 - num2
    st.text(f"O resultado da subtração entre eles é {result4}")
    st.title("Obrigado!")