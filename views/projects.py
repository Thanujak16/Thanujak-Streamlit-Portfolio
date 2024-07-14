import streamlit as st

col1, col2 = st.columns(2, gap="large", vertical_alignment="center")

with col1:
    st.image("assets/airbnb.png")
    st.write("Airbnb Project")
    st.write("Tech Stack: Python, Google Sheets, Jupyter Notebook, Google Data Studio")
    st.write(
        """
        - Conducted comprehensive data analysis and visualization on Airbnb listings data using Python libraries
        - Identified key market trends, pricing strategies, and customer preferences
        - Used the data loaded from Google Sheets and Utilized Google Looker Studio for interactive, visually engaging dashboards.
        """
    )
    airbnb = '[@Airbnb](https://github.com/Thanujak16/Airbnb)'
    st.write("Project Link")
    st.markdown(airbnb, unsafe_allow_html=True)

with col2:
    st.write("\n")
    st.image("assets/download.jpeg")
    st.write("Titanic Analysis")
    st.write("Tech Stack: Python, Jupyter Notebook, Tableau")
    st.write(
        """
        - Conducted in-depth analysis of Titanic passenger data, exploring correlations between survival rates and socio-demographic factors such as passenger class, gender, and age.
        - Utilized Python programming skills to preprocess and analyze the dataset, uncovering insights into survival probabilities based on variables such as family size (sibsp and parch), fare paid, and embarkation point.
        - Employed Excel for visualizing and presenting findings, revealing trends such as the higher survival rates among females, passengers from higher classes, and those traveling alone.
        """
    )