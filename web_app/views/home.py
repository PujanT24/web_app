import streamlit as st
import backend

col1, col2, = st.columns(2)


st.title("City Budget of Philadelphia")
st.divider()
st.markdown("")

st.header("What is budget?")
st.write("A budget is a financial plan that estimates expected income and expenses over a specific period of time. It acts as a roadmap to manage resources,control spending, and achieve short- or long-term goals.")
st.write("Implementing the city budget is a yearly process where mayor work with every department to review and draft a budget for the next fiscal year based on how much each categories need it. The Mayor presents that budget to the city council for approval. Participation for the public is also an important part of the budgeting process and it is encouraged to see if that budget is covering the needs of our community.  ")

st.header("Roles and Responsibility")
st.write("Every year, Philadelphia puts together a financial plan to keep the city running from July 1st through June 30th. The process starts with the Mayor collaborating with city departments to map out spending priorities, but it takes a team effort, including everyday residents to make sure the final plan truly serves the community. ")
st.write("• The Mayor (Executive Role): Takes the lead by drafting the initial plan and handing it over to the City Council.")
st.write("• The City Council (Legislative Role): Reviews the proposal, listens to what residents have to say, makes adjustments where needed, and votes to officially approve it. ")
st.write("• The Community (Public Role): Holds the real power by electing city leaders and speaking up during public hearings or reaching out to officials directly.")

st.header("Funding Sources")
st.write("By law, Philadelphia must balance its budget so that spending never exceeds its income. The city relies on three main funding streams:")
st.write(" • Grants: Dedicated money provided by the state, federal government, or private groups that must be spent on specific projects.")
st.write(" • Service Fees: Charges collected for specific city services to help cover the costs of running them.")
st.write(" • Taxes: Revenue gathered from local property, sales, and business taxes to fund public resources.")
st.title(" ")

st.write("Sources: " )
st.write("https://sslc.gov/504/City-Budget-Basics")
st.write("https://philly-stat-360.phila.gov/pages/budget  ")