# kt_project# AI Knowledge Transfer Assistant

Live Demo: https://ktproject-uodzgbvsjg7wvcizecg9pw.streamlit.app/

## Overview

The AI Knowledge Transfer Assistant is a Retrieval-Augmented Generation (RAG) application that helps users understand software projects by answering questions about the uploaded source code.

The application accepts a ZIP file containing a software project, extracts its contents, processes the project files, creates vector embeddings, and stores them in a vector database. When a user asks a question, the system retrieves the most relevant code and documentation before generating an answer using Google's Gemini model.

The responses are grounded in the uploaded project instead of relying only on the language model's general knowledge.

---

## Features

- Upload a software project as a ZIP file
- Automatically extract and scan project files
- Read source code and documentation
- Split files into semantic chunks
- Generate embeddings using Google Gemini
- Store embeddings in ChromaDB
- Retrieve relevant project context using semantic search
- Answer questions using Retrieval-Augmented Generation (RAG)
- Display the source files used to generate each answer

---

## Project Workflow

1. Upload a ZIP file containing the project.
2. Extract the uploaded project.
3. Scan all supported files.
4. Read the contents of each file.
5. Split the contents into smaller chunks.
6. Generate vector embeddings for every chunk.
7. Store embeddings in ChromaDB.
8. Accept a user question.
9. Retrieve the most relevant project chunks.
10. Generate an answer using Gemini based on the retrieved context.

---

## Technology Stack

- Python
- Streamlit
- Google Gemini API
- ChromaDB
- LangChain Text Splitters
- PyMuPDF
- python-docx

---

## Project Structure

```
kt_project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── loaders/
│   ├── zip_loader.py
│   ├── code_loader.py
│   └── document_loader.py
│
├── rag/
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── search.py
│   └── prompt.py
│
└── .streamlit/
    └── config.toml
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/deekshith2301/kt_project.git
```

Move into the project directory.

```bash
cd kt_project
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application.

```bash
streamlit run app.py
```

---

## Usage

1. Launch the application.
2. Upload a ZIP file containing a software project.
3. Wait for the knowledge base to be created.
4. Enter a question about the uploaded project.
5. View the generated answer and the corresponding source files.

---

## Example Questions

- Explain the project architecture.
- How does authentication work?
- Describe the database layer.
- What libraries are used in this project?
- Explain the API workflow.
- Which files are responsible for user authentication?
- Summarize the project.

---

## Future Improvements

- Guardrails for input validation
- Human-in-the-loop approval workflow
- Conversation history
- Support for additional file formats
- Deployment with Docker
- Multi-project knowledge base

---

## Author

Sai Deekshith Nadendla
