from langchain_core.prompts import PromptTemplate
from helper import get_llm
from structure import ExpanderStruct


class QueryExpander:

    def __init__(self):

        # self.prompt = PromptTemplate(
        #     input_variables=["query"],
        #     template="""
        #     Expand the following technical query into a more detailed semantic search query.
        #     Make it more detailed so that it can be used for searching everything about the given topic.
        #     Only exapand the query by details about what is being asked dont unnecessary things.
        #     Only output the detailed query.
        #     Orignal Query:
        #     {query}
        #     """
        # )

        self.prompt = PromptTemplate(
            input_variables=["query"],
            template='''
            You are an expert semantic query expansion engine optimized for vector databases, embedding-based retrieval, RAG pipelines, hybrid search systems, and knowledge retrieval.

            Your task is to transform a short, vague, incomplete, or ambiguous user query into a rich semantic retrieval query that maximizes embedding recall and contextual relevance.

            ## Core Objectives

            1. Preserve the original user intent exactly.
            2. Expand the query semantically using:
            - related terminology
            - domain-specific vocabulary
            - synonymous concepts
            - implicit technical context
            - likely associated technologies
            - alternate phrasings
            - abbreviations and expanded forms
            - implementation-related language
            - conceptual dependencies
            3. Infer the likely domain automatically.
            4. Adapt depth and terminology dynamically:
            - simple/general topics → broader semantic context
            - highly technical topics → precise expert terminology
            5. Generate text optimized for:
            - dense vector embeddings
            - semantic similarity retrieval
            - hybrid BM25 + vector retrieval
            - chunk recall in RAG systems
            6. Include contextual descriptors rather than keyword stuffing.
            7. Avoid changing the user's meaning or introducing unrelated topics.
            8. Prioritize retrieval usefulness over readability.


            ## Output Style Rules

            - Output ONLY the expanded semantic query.
            - Do NOT explain.
            - Do NOT summarize.
            - Do NOT use bullet points.
            - Generate one dense retrieval-optimized paragraph.
            - Include both concise and detailed terminology naturally.
            - Maintain high semantic richness.
            - Use technically precise wording when appropriate.
            - Include probable contextual intent behind the query.
            - Include related entities, methods, tools, and concepts when strongly relevant.

            Orignal Query:
            {query}        
            '''
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
    # print(a.expand("What is the process known as decoherence in quantum systems?"))
    print(a.expand("shoes"))

    





