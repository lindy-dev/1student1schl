import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to 1Student1School! A school of multi-agent teachers hyper-personalized to teach you!👋")

st.sidebar.success("Select a program above.")

st.markdown(
    """
    # What is 1Student1School?

    1Student1School A school of multi-agent teachers hyper-personalized to teach you!👋
    ## Features
    - **Privacy first**: We prioritize student privacy and data security, ensuring a safe learning environment. 
    - **Multi-Agent Teachers**: We employ a team of AI agents, each specializing in different subjects, to provide comprehensive education.
    - **Interactive Learning**: Our platform includes interactive tools and resources to engage students and enhance their learning experience.
    

"""
)
