import fitz  # PyMuPDF
from docx import Document


class DocumentLoader:

    def read_file(self, file_path):

        if file_path.endswith(".py"):
            return self.read_text(file_path)

        elif file_path.endswith(".md"):
            return self.read_text(file_path)

        elif file_path.endswith(".txt"):
            return self.read_text(file_path)

        elif file_path.endswith(".json"):
            return self.read_text(file_path)

        elif file_path.endswith(".pdf"):
            return self.read_pdf(file_path)

        elif file_path.endswith(".docx"):
            return self.read_docx(file_path)

        return ""

    def read_text(self, file_path):

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        except:
            return ""

    def read_pdf(self, file_path):

        text = ""

        try:
            pdf = fitz.open(file_path)

            for page in pdf:
                text += page.get_text()

            pdf.close()

        except:
            pass

        return text

    def read_docx(self, file_path):

        text = ""

        try:
            doc = Document(file_path)

            for para in doc.paragraphs:
                text += para.text + "\n"

        except:
            pass

        return text