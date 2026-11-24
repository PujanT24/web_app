import streamlit as st
from numpy.random import default_rng as rng
import backend





data = backend.create_df("data/data.csv")
art = backend.create_df("data/art.csv")
commercial = backend.create_df("data/commercial.csv")
courts = backend.create_df("data/courts.csv")
emergency = backend.create_df("data/emergency.csv")
govt = backend.create_df("data/govt.csv")
housing = backend.create_df("data/housing.csv")
immigration = backend.create_df("data/immigration.csv")
libraries = backend.create_df("data/libraries.csv")
mental = backend.create_df("data/mental.csv")
parks = backend.create_df("data/parks.csv")
police = backend.create_df("data/police.csv")
public_health = backend.create_df("data/health.csv")
school = backend.create_df("data/school.csv")
street = backend.create_df("data/street.csv")
trash = backend.create_df("data/trash.csv")
youth = backend.create_df("data/youth.csv")
yearly = backend.create_df("data/yearly.csv")


st.title("City Budget of Philadelphia")
st.divider()

st.header("Changes in Budget Every Year")
st.line_chart(yearly, x = "Year", y = "Funds (in Billion)", color = "green")

st.divider()
col1, col2, = st.columns(2)
with col1:
    st.title("Distribution of Categories")
    view = st.segmented_control("View", ["Chart", "Data"], default="Chart")

    if view == "Data":
        st.dataframe(data)
    else:
        st.bar_chart(data, x = "category", y = "total", sort = "-total", color = "red")

    st.header("Description of this data")
    st.write(data.describe())
    st.write("Across all 16 budget categories, the average is dollar 875.7 million, while the median is dollar 299.8 million. ")



with col2:
    st.title("Distribution by Categories")

    if "category" not in st.session_state:
        st.session_state.category = None

    action = st.menu_button("Category", options= ["Arts & Culture", "Commercial Corridors & Small Businesses", "Courts & the Justice System", "Emergency Services", "Government Operations", "Housing & Homeless Services", "Immigration Services", "Libraries", "Mental Health & Substance Use Services", "Parks & Recreation", "Police", "Public Health Centers", "Schools & Early Childhood Education", "Streets", "Trash & Sanitation", "Youth Services"])
    if action is not None:
        st.session_state.category = action

    category = st.session_state.category

    if category:
        st.subheader(category)



    if category == "Arts & Culture":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="arts_view")

        if view == "Data":
            st.dataframe(art)
        else:
            st.bar_chart(art, x = "class", y = "total", sort = "-total")
        


    if category == "Commercial Corridors & Small Businesses":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="commercial_view")

        if view == "Data":
            st.dataframe(commercial)
        else:
            st.bar_chart(commercial, x = "class", y = "total", sort = "-total")


            
    if category == "Courts & the Justice System":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="courts_view")

        if view == "Data":
            st.dataframe(courts)
        else:
            st.bar_chart(courts, x = "class", y = "total", sort = "-total")


            
    if category == "Emergency Services":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="emergency_view")

        if view == "Data":
            st.dataframe(emergency)
        else:
            st.bar_chart(emergency, x = "class", y = "total", sort = "-total")


        
    if category == "Government Operations":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="govt_view")

        if view == "Data":
            st.dataframe(govt)
        else:
            st.bar_chart(govt, x = "class", y = "total", sort = "-total")


        
    if category == "Housing & Homeless Services":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="housing_view")

        if view == "Data":
            st.dataframe(housing)
        else:
            st.bar_chart(housing, x = "class", y = "total", sort = "-total")



    if category == "Immigration Services":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="immigration_view")

        if view == "Data":
            st.dataframe(immigration)
        else:
            st.bar_chart(immigration, x = "class", y = "total", sort = "-total")



    if category == "Libraries":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="library_view")

        if view == "Data":
            st.dataframe(libraries)
        else:
            st.bar_chart(libraries, x = "class", y = "total", sort = "-total")



    if category == "Mental Health & Substance Use Services":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="mental_view")

        if view == "Data":
            st.dataframe(mental)
        else:
            st.bar_chart(mental, x = "class", y = "total", sort = "-total")



    if category == "Parks & Recreation":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="parks_view")

        if view == "Data":
            st.dataframe(parks)
        else:
            st.bar_chart(parks, x = "class", y = "total", sort = "-total")



    if category == "Police":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="police_view")

        if view == "Data":
            st.dataframe(police)
        else:
            st.bar_chart(police, x = "class", y = "total", sort = "-total")



    if category == "Public Health Centers":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="health_view")

        if view == "Data":
            st.dataframe(public_health)
        else:
            st.bar_chart(public_health, x = "class", y = "total", sort = "-total")



    if category == "Schools & Early Childhood Education":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="school_view")

        if view == "Data":
            st.dataframe(school)
        else:
            st.bar_chart(school, x = "class", y = "total", sort = "-total")



    if category == "Streets":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="street_view")

        if view == "Data":
            st.dataframe(street)
        else:
            st.bar_chart(street, x = "class", y = "total", sort = "-total")



    if category == "Trash & Sanitation":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="trash_view")

        if view == "Data":
            st.dataframe(trash)
        else:
            st.bar_chart(trash, x = "class", y = "total", sort = "-total")



    if category == "Youth Services":
        view = st.segmented_control("View", ["Chart", "Data"], default="Chart", key="youth_view")

        if view == "Data":
            st.dataframe(youth)
        else:
            st.bar_chart(youth, x = "class", y = "total", sort = "-total")




