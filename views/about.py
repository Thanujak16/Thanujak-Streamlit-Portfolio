import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/img2.jpg", width=200)

with col2:
    st.title("Thanuja K", anchor=False)
    st.write('An aspiring Data analyst enthusiast well versed in SQL, Excel and Data Studio')
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
    - Passionate fresh graduate with a solid 6-month track record in analytics.
    - Proficient in Python basics, adept at Excel, and with 2 years of experience in MS Office.
    - Ready to transform raw data into actionable insights
    - Excited to embark on a data-driven journey with your esteemed organization.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - Languages: Python, SQL, Excel
    - Visualization Tools: Tableau, PowerBI, Google Data Studio
    - Developer Tools: VS Code, PyCharm, Sublime Text Editor
    - Libraries: Pandas, Numpy, Matplotlib,Seaborn
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
    st.write("Jan. 2021 – Nov 2023")
    st.write("Bangalore,Karnataka")


# --- Certification and Achievements ---
st.write("\n")
st.subheader("Certification and Achievements", anchor=False)
col7, col8 = st.columns(2, gap="large", vertical_alignment="center")
with col7:
    st.subheader('Certification')
    git = '[@Excel Skills for Business: Essentials](https://www.coursera.org/account/accomplishments/verify/7BWAKJ5B56V8?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course)'
    st.markdown(git, unsafe_allow_html=True)

with col8:
    st.subheader('Achievements')
    st.write('Student Volunteer,National Service Scheme')
    st.write('Sep 2019 - Sep 2020 ')
