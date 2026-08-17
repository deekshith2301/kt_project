from langchain_text_splitters import RecursiveCharacterTextSplitter

class EmbeddingProcessor:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            split_text = self.splitter.split_text(
                document["content"]
            )

            for text in split_text:

                chunks.append(
                    {
                        "text": text,
                        "source": document["path"]
                    }
                )

        return chunks