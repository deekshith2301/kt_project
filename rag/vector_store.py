import os
import chromadb

from dotenv import load_dotenv
from google import genai

load_dotenv()


class VectorStore:

    def __init__(self, reset=False):

        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        self.chroma = chromadb.PersistentClient(
            path="chroma_db"
        )

        if reset:
            try:
                self.chroma.delete_collection("kt_project")
            except Exception:
                pass

        self.collection = self.chroma.get_or_create_collection(
            name="kt_project"
        )

    def add_documents(self, chunks):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for index, chunk in enumerate(chunks):

            response = self.client.models.embed_content(
                model="models/gemini-embedding-001",
                contents=chunk["text"]
            )

            ids.append(str(index))
            documents.append(chunk["text"])
            embeddings.append(response.embeddings[0].values)
            metadatas.append(
                {
                    "source": chunk["source"]
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, query, k=5):

        response = self.client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=query
        )

        query_embedding = response.embeddings[0].values

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )