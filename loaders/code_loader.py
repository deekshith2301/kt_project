import os

class ProjectScanner:

    # File types we want to analyze
    SUPPORTED_EXTENSIONS = {
        ".py",
        ".java",
        ".js",
        ".ts",
        ".cs",
        ".cpp",
        ".c",
        ".md",
        ".txt",
        ".pdf",
        ".docx",
        ".json",
        ".yaml",
        ".yml",
        ".xml"
    }

    # Folders we don't want to scan
    IGNORE_FOLDERS = {
        "__pycache__",
        ".git",
        ".idea",
        ".vscode",
        "venv",
        "env",
        "node_modules"
    }

    def scan_project(self, project_path):

        files = []

        for root, dirs, filenames in os.walk(project_path):

            # Ignore unwanted folders
            dirs[:] = [
                d for d in dirs
                if d not in self.IGNORE_FOLDERS
            ]

            for file in filenames:

                extension = os.path.splitext(file)[1].lower()

                if extension in self.SUPPORTED_EXTENSIONS:

                    files.append({
                        "name": file,
                        "path": os.path.join(root, file),
                        "extension": extension
                    })

        return files