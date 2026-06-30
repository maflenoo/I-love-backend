import streamlit as st

st.title("Backend is better than AI")

num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

result = num1 + num2

st.write("### Result:")
st.success(f"The sum is: {result}")