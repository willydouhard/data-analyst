from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


instructions = """You are an assistant running cleaning CSV files.

You will use code interpreter to run do the cleaning.

To clean the files, check that the columns contain valid country names. If you can correct it correct it otherwise flag it.

Once the cleaning is done, you will print the head of the table giving an overview of the cleaned content and make the cleaned file downloadable.
"""

tools = [
    {"type": "code_interpreter"},
    {"type": "file_search"}
]

# file = openai_client.files.create(
#   file=open("tesla-stock-price.csv", "rb"),
#   purpose='assistants'
# )


assistant = openai_client.beta.assistants.create(
    model="gpt-4o",
    name="Data Analysis Assistant",
    instructions=instructions,
    temperature=0.1,
    tools=tools,
    # tool_resources={
    #     "code_interpreter": {
    #     "file_ids": [file.id]
    #     }
    # }
)

print(f"Assistant created with id: {assistant.id}")