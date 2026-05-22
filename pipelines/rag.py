import warnings
warnings.filterwarnings("ignore")
from helper import ingest
from helper import EmbeddingModel
from vectorstore import VectorStore
from helper import Retriever
from QueryExpander import QueryExpander
from langchain_core.prompts import PromptTemplate
from helper import get_llm
from structure import RagOutput
import json

class RAGPipeline:

    def __init__(self, path):

        embedding_model = EmbeddingModel().get()

        self.vector_store = VectorStore(
            embedding_model
        )

        self.documents = ingest(path=path, chunk_size=250, overlap_size=100)
        self.vector_store.build(self.documents)

        self.retriever = Retriever(
            self.vector_store
        )

        self.expander = QueryExpander()
        
        self.llm = get_llm(model='llama').with_structured_output(RagOutput)
        self.rag_prompt = PromptTemplate(
            input_variables=['docstring', 'question'],
            template='''
            You are an assistant. Your job is to answer the user's question based on the information provided to you.
            You must only answer the question from the given information.
            Do not create anything on your own.

            Given Information: {docstring}
            User's Question: {question}

    '''
        )

    def strategy_a(self, query):

        return self.retriever.retrieve(query)

    def strategy_b(self, query):

        expanded_query = self.expander.expand(query)

        return self.retriever.retrieve(expanded_query)


    def rag(self, query, strategy='a'):
        if strategy == 'a':
            docs = self.strategy_a(query)
        elif strategy == 'b':
            docs = self.strategy_b(query)
        # print(docs)
        documents = [item["document"] for item in docs]

        docstring = ' '.join(documents)
        formatted_prompt = self.rag_prompt.format(docstring=docstring, question = query)
        response = self.llm.invoke(formatted_prompt)
        return response
    
    def combine_rag_strategies(self, query) -> dict:
        outputs = {}
        resp1 = self.rag(query, strategy='a')
        resp2 = self.rag(query, strategy='b')
        outputs[query] = {
            'strategy_a': resp1.answer,
            'strategy_b': resp2.answer,
        }
        # with open('rag_outputs.json', 'w') as f:
        #     f.write(json.dumps(
        #         outputs,
        #         indent=2
        #     ))
        return outputs


