import streamlit as st
import backend




st.set_page_config(page_title="City Budget of Philadelphia", layout="wide")


#link views on other python scripts
intro = st.Page("views/intro.py", title=":rainbow[Introduction]", icon="👌", default=True)
home = st.Page("views/home.py", title=":rainbow[Home]", icon="🏡")
philadelphia = st.Page("views/philadelphia.py", title=":rainbow[Philadelphia]", icon="🌆")
data = st.Page("views/data.py", title=":rainbow[Data]", icon="📈")
resources = st.Page("views/resources.py", title = ":rainbow[Resources]", icon = "🔡")

#navigation bar
pg = st.navigation([intro, home, philadelphia, data, resources])


#run the pages
pg.run()
