# from typing_extensions import Annotated,TypedDict
from pydantic import BaseModel, Field

class ExpanderStruct(BaseModel):
    '''The structure for how the expanded and detailed query should be given in output'''
    query: str = Field(description="Detailed semantic search query.")