import streamlit as st
from collections import Counter
from dotenv import load_dotenv

from loaders.zip_loader import ZipLoader
from loaders.code_loader import ProjectScanner
from loaders.document_loader import DocumentLoader

from rag.embeddings import EmbeddingProcessor
from rag.vector_store import VectorStore
from rag.search import ProjectSearch

load_dotenv()

st.set_page_config(
    page_title="KT Assistant",
    layout="wide"
)

st.title("📚 AI Knowledge Transfer Assistant")
st.write("Upload a project ZIP file and ask questions about the project.")

uploaded_file = st.file_uploader(
    "Choose ZIP File",
    type=["zip"]
)

if uploaded_file:

    # -----------------------------
    # Save & Extract ZIP
    # -----------------------------
    loader = ZipLoader()

    zip_path = loader.save_zip(uploaded_file)
    extract_path = loader.extract_zip(zip_path)

    st.success("✅ Project uploaded successfully!")

    st.write("### Extraction Folder")
    st.code(extract_path)

    # -----------------------------
    # Scan Project
    # -----------------------------
    scanner = ProjectScanner()

    files = scanner.scan_project(extract_path)

    st.subheader(f"📂 Total Files : {len(files)}")

    counter = Counter()

    for file in files:
        counter[file["extension"]] += 1

    st.subheader("📊 Project Summary")

    for ext, count in sorted(counter.items()):
        st.write(f"**{ext}** : {count}")

    # -----------------------------
    # Read Documents
    # -----------------------------
    document_loader = DocumentLoader()

    documents = []

    with st.spinner("Reading project files..."):

        for file in files:

            content = document_loader.read_file(file["path"])

            if content.strip():

                documents.append(
                    {
                        "path": file["path"],
                        "content": content
                    }
                )

    st.success(f"✅ Loaded {len(documents)} documents")

    # -----------------------------
    # Preview
    # -----------------------------
    st.subheader("📄 Document Preview")

    for doc in documents[:5]:

        with st.expander(doc["path"]):

            st.text(doc["content"][:700])

    # -----------------------------
    # Create Knowledge Base
    # -----------------------------
    with st.spinner("Creating Knowledge Base..."):

        processor = EmbeddingProcessor()

        chunks = processor.chunk_documents(documents)

        st.write(f"Chunks Created : {len(chunks)}")

        vector_db = VectorStore(reset=True)

        vector_db.add_documents(chunks)

    st.success("✅ Knowledge Base Created Successfully")

    st.divider()

    # -----------------------------
    # Ask Questions
    # -----------------------------
    st.header("💬 Ask Questions About Your Project")

    question = st.text_input(
        "Example: Explain the authentication module."
    )

    if question:

        with st.spinner("Searching project..."):

            search = ProjectSearch()

            result = search.ask(question)

        st.subheader("🤖 Answer")

        st.write(result["answer"])

        st.subheader("📁 Source Files")

        if result["sources"]:

            for source in result["sources"]:
                st.write(f"📄 {source}")

        else:

            st.write("No source files found.")