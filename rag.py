import warnings
warnings.filterwarnings("ignore")
from helper import ingest
from helper import EmbeddingModel
from vectorstore import VectorStore
from helper import Retriever
from QueryExpander import QueryExpander


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

    def strategy_a(self, query):

        return self.retriever.retrieve(query)

    def strategy_b(self, query):

        expanded_query = self.expander.expand(query)

        return self.retriever.retrieve(expanded_query)