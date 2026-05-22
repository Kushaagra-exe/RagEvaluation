from typing_extensions import Annotated,TypedDict
from pydantic import BaseModel, Field

class ExpanderStruct(BaseModel):
    '''The structure for how the expanded and detailed query should be given in output'''
    query: str = Field(description="Detailed semantic search query.")



class Generated_qna(BaseModel):
    '''The structure for how question and answer should be generated from the given information'''
    question: str = Field(description="the question generated from the given information.")
    answer: str = Field(description="the answer of the question generated from the given information.")

class RagOutput(BaseModel):
    '''The structure for how the answer from the given information should be generated'''
    answer: str = Field(description="the answer of the question generated from the given information.")