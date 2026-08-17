import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

from rag.vector_store import VectorStore
from rag.prompt import SYSTEM_PROMPT

load_dotenv()


class ProjectSearch:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        self.db = VectorStore()

    def ask(self, question):

        results = self.db.search(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = "\n\n".join(documents)

        prompt = f"""
{SYSTEM_PROMPT}

=========================
PROJECT CONTEXT
=========================

{context}

=========================
QUESTION
=========================

{question}

Instructions:

1. Answer ONLY using the project context.
2. Do not make up information.
3. If the answer is unavailable, reply:

"I couldn't find this information in the uploaded project."

4. Mention the relevant file names whenever possible.
5. Keep the answer clear and concise.
"""

        response = None

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model="models/gemini-3.5-flash",
                    contents=prompt
                )

                break

            except ServerError:

                if attempt == 2:
                    raise

                time.sleep(3)

        sources = []

        for metadata in metadatas:

            source = metadata.get("source")

            if source not in sources:
                sources.append(source)

        return {
            "answer": response.text,
            "sources": sources
        }