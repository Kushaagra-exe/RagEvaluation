from langchain_core.prompts import PromptTemplate
from helper import get_llm
from structure import ExpanderStruct


class QueryExpander:

    def __init__(self):

        self.prompt = PromptTemplate(
            input_variables=["query"],
            template="""
            Expand the following technical query into a more detailed semantic search query.
            Make it more detailed so that it can be used for searching everything about the given topic.
            Only exapand the query by details about what is being asked dont unnecessary things.
            Only output the detailed query.
            Orignal Query:
            {query}
            """
        )

        
        self.llm = get_llm(model='llama').with_structured_output(ExpanderStruct)

    
    def expand(self, query):
        formatted_prompt = self.prompt.format(query=query) 
        # print(formatted_prompt, '\n--------')       
        response = self.llm.invoke(formatted_prompt)
        # print(response,'\n--------')
        return response.query
    


if __name__ == '__main__':
    a = QueryExpander()
    # print(a.expand("quantum computing techniques"))
    print(a.expand("shoes"))

    





