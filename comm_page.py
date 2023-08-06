import streamlit as st
from config import *

def comm():
    st.header("✉️ Share your findings to data owners")
    system_prompt = """Assistant is the lead data steward in a company. He monitors the overall data quality performance for the company and he's in charge of communicating
    his findings to the data owners. He can identify the priority of the data issues, and can provide data quality improvement guidance to data owners."""
    data_owner = st.text_input("Who do you want to send the communication message to?")
    urgency_option = st.selectbox("What's the urgency level of this communication message?", options=["Low Urgency", "Medium Urgency", "High Urgency"])
    instruction = f"""I will provide you with a data quality report. Please write an email to {data_owner} communicate this findings to the data owners. Be specific on the issues in the data by giving the email recevier examples. 
    This communication is {urgency_option}. Draft the email as if you are the data steward. Here's the data quality report: """
    
    if st.button("Generate Communication Message", type= "primary"):
        # Check if the text is available in the session state
        if 'generated_text' in st.session_state:
            # Access the generated text from the session state
            dq_report = st.session_state.generated_text
            response = llm([
                SystemMessage(content=system_prompt),
                HumanMessage(content=instruction + dq_report)
            ]).content
            st.markdown(response)
        else:
            "Please generate the data quality report first."

