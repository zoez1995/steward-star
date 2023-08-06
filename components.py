## IMPORT STREAMLIT
import streamlit as st
import pandas as pd

## PAGE HEADER
def setup_page():
    st.set_page_config(
        page_title = "StewardStar - The AI Data Quality Controller",
        layout = "wide",
        page_icon = "💫",
        initial_sidebar_state="expanded",
    )

## HEADER IMAGE
def display_logo():
    st.image("data/header_image.png", width = 800)

# WELCOME MESSAGE
def welcome_message():
    st.header("💫 Welcome to StewardStar - The Data Quality Controller Powered by GenAI 🧙")

# SITE DESCRIPTION
def site_description():
    st.markdown('**:blue[StewardStar can help you understand the data better than the data owner. Simply give StewardStar some context, such as a data schema file of your database, and StewardStar will help you diagnose your data!]**')

# UPLOAD CONTEXT FILE
def context_file():
    uploaded_file = st.file_uploader("Upload your context file below. The context file can be a data schema file of your database or a data template you want StewardStar to refer to. You can skip this step if you don't want to use a context file.", type=["csv", "txt"])
    df_string = ""
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain": 
            df = pd.read_csv(uploaded_file, sep="\t")
        elif uploaded_file.type ==  "text/csv":
            df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        df_string = df.to_string()
        df_string.replace(" ","")
    return df_string



# UPLOAD DATA FILES
def file_container():
    # Create a file uploader widget that accepts multiple files
    uploaded_files = st.file_uploader("Please upload your data files below.", type=["csv", "xlsx", "txt"], accept_multiple_files=True)
    result = []
    if uploaded_files is not None:
        # Iterate through the uploaded files and read them
        for uploaded_file in uploaded_files:
            # Get some information about the uploaded file
            # file_info = f"FileName: {uploaded_file.name}, FileSize: {uploaded_file.size}"
            # st.write(file_info)
            # Read the uploaded CSV file
            if uploaded_file.type == "text/plain": 
                df = pd.read_csv(uploaded_file, sep="\t")
            elif uploaded_file.type ==  "text/csv":
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file, index_col=None, engine="openpyxl")
            # st.session_state[uploaded_file.name] = df
            result.append(df)
    return result

# GENERATE DATA PREVIEW
def data_preview(data_list):
    for df in data_list:
        st.dataframe(df.head(20))
