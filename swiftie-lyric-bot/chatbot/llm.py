import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4-turbo"
    )