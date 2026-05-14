from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import warnings
# from vertexai.language_models import TextEmbeddingModel
# from vertexai.generative_models import GenerativeModel

warnings.filterwarnings("ignore")

import os
from dotenv import load_dotenv
load_dotenv()
API = os.environ['GROQ_API_KEY']
gAPI = os.environ['GOOGLE_API_KEY']


class EmbeddingModel:

    def __init__(self, model='allminilm'):
        if model=='allminilm':
            self.embedding_model = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
        if model=='baai':
            self.embedding_model = HuggingFaceEmbeddings(
                model_name='BAAI/bge-small-en-v1.5'
            )
            
        elif model=='vertex':
            self.embedding_model = TextEmbeddingModel(
                'text-embedding-004'
            )


    def get(self):

        return self.embedding_model
    

def get_llm(model):
    if model =='oss':
        llm = ChatGroq(api_key=API, 
                       model="openai/gpt-oss-120b",
                        n=1
                       )
    elif model == 'gemini':
        llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite",
            max_retries=1,
            api_key = gAPI
        )
    elif model == 'llama':
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",

            max_retries=3,
            api_key = API
        )
    elif model == 'vertex':
        llm = GenerativeModel("gemini-1.5-flash-001")

    return llm



def ingest(path, chunk_size=250, overlap_size=100):

    loader = TextLoader(path, encoding="utf-8")

    documents = loader.load()

    print(f"Loaded {len(documents)} document(s)")
    # print(documents)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap_size
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    # for i, chunk in enumerate(chunks[:3]):
    #     print(f"\n--- Chunk {i+1} ---")
    #     print(chunk.page_content[:300])
    return chunks


# def vectorise():

class Retriever:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    def retrieve(self, query, top_k=3):

        return self.vector_store.search(
            query=query,
            top_k=top_k
        )

if __name__ == '__main__':
    a = ingest('Quantum computing.txt', chunk_size=500, overlap_size=10)






