from config import *

system_prompt = "Assistent is great at retrieving data from a hyperlink."
instruction = """I want you to give me a summary of the content of the hyperlink. Here's the hyperlink:
https://platform.openai.com/docs/api-reference/authentication"""

response = llm([
            SystemMessage(content=system_prompt),
            HumanMessage(content=instruction)
        ]).content
print(response)