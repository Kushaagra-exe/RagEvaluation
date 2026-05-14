from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()
API = os.environ['GROQ_API_KEY']

def get_llm(model):
    llm = ChatGroq(api_key=API, 
                    model="openai/gpt-oss-120b",
                    
                    )
    return llm