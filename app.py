import pandas as pd
import streamlit as st
from PIL import Image


def resize_to_square(image, size=70):
    return image.resize((size, size))

# Custom CSS for enhanced aesthetics
st.markdown("""
    <style>
    .main {background-color: #f5f5f5; padding-left: 0px; padding-right: 0px; h1, h2, h3, h4, h5, h6, p {color: #2c3e50;}}
    .sidebar .sidebar-content {background-color: #2c3e50; color: black; padding-right: 20px;}
    h1, h2, h3 {color: #FFFFF;}
    .stButton>button {background-color: #4CAF50; color: white;}
    </style>
    """, unsafe_allow_html=True)

# App Title
st.title("My Autobiography and Portfolio")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Portfolio", "Contact"])

# About Me Section
if page == "About Me":
    st.header("About Me")
    
    col1, col2 = st.columns(2)
    
    with col1:
        me = Image.open("me.jpg")
        st.image(me, width=200)
    with col2:
        cit = Image.open("cit logo.png")
        st.image(cit, width=200)
    
    # Write autobiography with expanding sections
    st.subheader("My Journey")
    with st.expander("Click to read more about my journey"):
        st.write("""
        Hi I am Adrian Claude S. Babatid a 4th year BS in Information Technology student from the Cebu Institute of Technology University 
        I am an aspiring programmer/developer/data analyst and hopefully I can be able to work for the industry once I graduate. I come from
        humble beginnings from my hometown Mactan, Lapu-Lapu City. I studied primary and secondary education in St. Alphonsus Catholic School
        that became pillars of how I am today. I am of 22 years of age and currently I am unemployed to focus on being a student.
        """)
    
    st.subheader("Hobbies and Interests")
    with st.expander("Click to learn about my hobbies and interests"):
        st.write("""
        Being a student is not enough I have a life outside of my studies. In my free time I play sports including basketball and I try to ride
        my bike as much as possible. I habitually play online games like Mobile Legends: Bang Bang and Valorant. I am an avid fan of series and dramas
        most notable Korean dramas and animes. To top it all off I stan Kpop idols like Twice, Red Velvet and etc. and also our very own Bini.
        """)


# Portfolio Section
elif page == "Portfolio":
    st.header("My Portfolio")
    
    st.subheader("Programming Languages")
    python = resize_to_square(Image.open("python.jpg"))
    css = resize_to_square(Image.open("css.png"), size=70)
    html = resize_to_square(Image.open("html.png"), size=70)
    js = resize_to_square(Image.open("js.png"), size=70)
    react = resize_to_square(Image.open("react.png"), size=70)
    java = resize_to_square(Image.open("java.jpg"), size=70)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.image(python, width=70)
    with col2:
        st.image(css, width=70)
    with col3:
        st.image(html, width=70)
    with col4:
        st.image(js, width=70)
    with col5:
        st.image(react, width=70)
    with col6:
        st.image(java, width=70)

    st.subheader("Project 1: FindNest")
    st.write("""
    Developed a Lost and Found app website for CIT-U as a capstone project using MERN stack.
    The website features a responsive design, user-friendly interface, and mobile application.
    """)
    st.image("findnest.jpg", caption="Web Development Project", use_column_width=True)
    
    st.subheader("Project 2: Noteaze")
    st.write("""
    Created a notes app with an edgy design using django framework. The website featured a responsive design
    with different features such as posting notes, adding photos and rich text and etc.
    """)
    st.image("noteaze.jpg", caption="Data Analysis Project", use_column_width=True)
    
    col7, col8 = st.columns(2)
# # Adding a bar chart for skills distribution
    with col7:
        st.subheader("Skills Distribution")
        skills = {
            'Python': 20,
            'HTML/CSS': 30,
            'JavaScript': 10,
            'Machine Learning': 15,
            'Data Analysis': 15,
            'Java/OOP': 10
        }
        st.bar_chart(skills)
    with col8:
        # Adding a line chart for project timelines
        st.subheader("Project Timelines in months")
        project_timeline = {
            'FindNest': 3,
            'Noteaze': 5
        }
        st.line_chart(project_timeline)

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    
    st.write("Feel free to reach out to me through the following platforms:")
    
    st.markdown("[acbabatid7@gmail.com](mailto:acbabatid7@gmail.com)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/claude-babatid-a87774326/)")
    st.markdown("[GitHub](https://github.com/Esclaud)")

    st.write("Or you can message me here")
    # Add a contact form with validation
    with st.form(key='contact_form'):
        name = st.text_input("Your Name", placeholder="Enter your name here")
        email = st.text_input("Your Email", placeholder="Enter your email here")
        message = st.text_area("Your Message", placeholder="Enter your message here")
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            if name and email and message:
                st.success(f"Thank you {name}! Your message has been sent.")
            else:
                st.error("Please fill out all fields before submitting.")




