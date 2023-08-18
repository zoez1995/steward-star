## IMPORT ALL NECESSARY COMPONENTS FROM CONFIG.PY AND UI.PY
from config import *
from components import *
from page_placeholder import *
from viz_page import *
from comm_page import *

setup_page()
def dq_page():
    ## RENDER UI COMPONENTS
    display_logo()
    welcome_message()
    site_description()
    # param set up
    st.subheader("📋 Generate Data Quality Report")
    context = context_file()
    st.write(context)
    data = file_container()
    data_preview(data)
    query = st.text_input("What's your question about the data you uploaded?")

    ## PROMPT 
    system_prompt = "Assistant is a highly skilled Data Quality Analyst. He can answer any question you have about your data. He's very detail oriented and always provide the accurate analysis."
    instruction = """I want you to act as a Data Steward in charge of monitoring and improving the data quality at your company. 
    You will have access to several data tables at the company along with table schemas. 
    These data tables can have text or numeric data. 
    There may be some additional metadata about the tables also given to you. 
    You will have to use this information, along with your judgement, on what values make sense for the data. 
    You will have to understand each table individually and how it relates to other tables holistically. 
    Also understand the relationships between columns. After understanding the data, your job will be to generate a Data Quality (DQ) report for each data set I provided and answer my questions about the data.
        1. Assess the Data Quality (DQ) for the DQ dimensions of accuracy, completeness, consistency, conformity and consistency. 
        2. Create a detailed DQ Report addressing these DQ dimensions with appropriate DQ metrics. Examples could be - percentage of null records etc. DQ report should be in a document format with clear section headers.
        3. Flag anomalous records. In the DQ report, create a section for anomalous records. Anomalies could be data that doesn't fit real-world expectations, such as longitude values that are negative.
        4. Suggest ways that to replace anomalous data with reasonable approximations - you could look at techniques such as interpolation
    If I provide any context about the data to you, you must ensure the data complies with the context. For example, if I give you a table schema as the context, you must check if the columns, especially primary keys, are in the data, and matches the table schema. 
    Below is the context about the data I may want to ask you questions about:"""


    ## HANDLE USER INPUT
    if query:
        st.write(f"Your question is: {query} Now click the Generate Report button.")
        
    if data is not None:
        data_prompt = ""
        count = 1
        for file in data:
            file_string = file.to_string()
            data_prompt = data_prompt + f'Data set {count} is: ' + file_string + f'That is all for Data set {count}.'
            count += 1

    ## DISPLAY RESPONSE 
    if st.button("Generate Report", type="primary"):
        response = llm([
            SystemMessage(content=system_prompt),
            HumanMessage(content=instruction + context + "Here's my data: " + data_prompt + "Read the data above and answer my question: " + query)
        ]).content
        # llm = openai.ChatCompletion.create(**parameters)
        # llm_dict = dict(llm)
        # content = llm_dict['choices'][0]['message']['content']
        st.divider()
        st.subheader("Data Quality Report")
        st.markdown(response)
        st.session_state.generated_text = response


# Create a dictionary of pages
pages = {
    "Diagnose Data": dq_page,
    "Visualize Data": viz,
    "Generate Communication": comm,
}

# Create a sidebar for navigation
st.sidebar.title('Site Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the corresponding page function based on the user's selection
page = pages[selection]
page()