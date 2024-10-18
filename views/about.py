import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/img2.jpg", width=200)

with col2:
    st.title("Thanuja K", anchor=False)
    st.write("Operations Specialist (Analyst)@ Design Cafe| Sid's Farm Pvt Ltd | | Data Science | MS Excel | Data Integration, and Automation In Smartsheet | Power BI | Process Excellence | MBA Food Business(Analytics).")
    col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
    with col3:
        github = '[@GitHub](https://github.com/Thanujak16)'
        linkedin = '[@Linkedin](https://www.linkedin.com/in/thanuja-kedila/)'
        st.markdown(github, unsafe_allow_html=True)
        st.markdown(linkedin, unsafe_allow_html=True)
    with col4:
        whatsapp = '[@Whatsapp](https://wa.me/+919741366689)'
        st.markdown(whatsapp, unsafe_allow_html=True)
    st.subheader("My Resume")
    resume = '[@Resume](https://drive.google.com/file/d/1eKoRKIuoQabVkJGS3qVmw_0vbCkfE2mt/view?usp=sharing)'
    st.markdown(resume, unsafe_allow_html=True)
# --- QUALIFICATIONS ---
st.write("\n")
st.subheader("Qualifications", anchor=False)
st.write(
    """
    - Passionate MBA graduate with 11 months of analytics experience, specializing in Smartsheet, Excel, and Python.
    - Proven ability to create dashboards, reports, and workflows that optimize updating customer details, customer tracking and project management. 
    - Experienced in analyzing data and providing strategic insights to improve decision-making.
    - Skilled in market research and data visualization, with hands-on experience using Tableau and Looker Studio
    - Ready to contribute to data-driven solutions and help organizations turn raw data into actionable strategies.
    - Proficient in MS Office, Google Sheets, SQL, and Python libraries like Pandas and Matplotlib.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - Languages: Python, SQL
    - Databases: Smartsheets, Google Sheets, Excel
    - Visualization Tools: Tableau, PowerBI, Google Data Studio
    - Developer Tools: VS Code, PyCharm, Sublime Text Editor
    - Libraries: Pandas, Numpy, Matplotlib,Seaborn, MySQL Connector
    """
)

# --- Education ---
st.write("\n")
st.subheader("Education", anchor=False)
col5, col6 = st.columns(2, gap="large", vertical_alignment="center")
with col5:
    st.subheader("MBA in Food Business (Analytics and Marketing)", anchor=False)
    st.write("Karnataka Veterinary, Animal and Fisheries Sciences University", anchor=False)

with col6:
    st.write("Jan. 2023 – Nov 2023")
    st.write("Bangalore,Karnataka")


# --- Certification and Achievements ---
st.write("\n")
st.subheader("Certification and Achievements", anchor=False)
col7, col8 = st.columns(2, gap="large", vertical_alignment="center")
with col7:
    st.subheader('Certification')
    bi = '[@Master in Power BI](https://drive.google.com/file/d/1r8r47penos7iZcoZhD7JmcVjMp3TXwMp/view?usp=drive_link)'
    st.markdown(bi, unsafe_allow_html=True)
    git = '[@Excel Skills for Business: Essentials](https://www.coursera.org/account/accomplishments/verify/7BWAKJ5B56V8?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course)'
    st.markdown(git, unsafe_allow_html=True)
    excel = '[@Excel Skills for Business: Intermediate I](https://www.coursera.org/account/accomplishments/verify/FRVYT9QX429E)'
    st.markdown(excel, unsafe_allow_html=True)
    tableau = '[@Fundamentals of Visualization with Tableau](https://www.coursera.org/account/accomplishments/verify/39BDWRCZHYDH)'
    st.markdown(tableau, unsafe_allow_html=True)

with col8:
    st.subheader('Achievements')
    st.write('Student Volunteer,National Service Scheme')
    st.write('Sep 2019 - Sep 2020 ')
