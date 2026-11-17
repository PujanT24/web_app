import streamlit as st
from numpy.random import default_rng as rng
import backend


st.title("City Budget of Philadelphia")

data = backend.create_df("data/data2.csv")

view = st.segmented_control("View", ["Chart", "Data"], default="Chart")

if view == "Data":
    st.dataframe(data)
else:
    st.bar_chart(data, x = "category", y = "total", sort = "-total",)

action = st.menu_button("Category", options= ["Arts & Culture", "Commercial Corridors & Small Businesses", "Courts & the Justice System", "Emergency Services", "Government Operations", "Housing & Homeless Services", "Immigration Services", "Libraries", "Mental Health & Substance Use Services", "Parks & Recreation", "Police", "Public Health Centers", "Schools & Early Childhood Education", "Streets", "Trash & Sanitation", "Youth Services"])

if action == "Arts & Culture":
    st.write("You chose Arts & Culture")

    st.balloons()