import streamlit as st
import backend

st.title("City Budget of Philadelphia")

st.markdown("I made this website to show the people living in Philly exactly how the city's money is being handled. It removes the mystery of government spending so everyday citizens can understand it. ")

st.image("assets/poster.png",400,400)
st.markdown("This shows residents whether their tax dollars are fixing local problems, and where the money goes.")


st.link_button("Home", "home")

