import streamlit as st
### DO NOT simply press run in streamlit.
### USE streamlit run[filename].py at the console

#Set the app title
st.title("My first streamlit app")

#Display text output
st.write('Welcome to my first streamlit app')

#Display a button
st.button('Reset', type='primary')
if st.button('Say Hello'):
  st.write("Why hello there")
else:
  st.write("Goodbye")

