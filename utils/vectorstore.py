from langchain_community.vectorstores import FAISS
import warnings
warnings.filterwarnings("ignore")

class VectorStore:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model
        self.db = None

    def build(self, documents):

        self.db = FAISS.from_documents(
            documents=documents,
            embedding=self.embedding_model
        )

    def search(self, query, top_k=3):

        results = self.db.similarity_search_with_score(
            query,
            k=top_k
        )

        formatted = []

        for doc, score in results:

            formatted.append({
                "score": float(score),
                "document": doc.page_content
            })

        return formatted

