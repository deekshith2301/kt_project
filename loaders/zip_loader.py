import os
import zipfile


class ZipLoader:
    def __init__(self, upload_folder="uploads", extract_folder="extracted"):
        self.upload_folder = upload_folder
        self.extract_folder = extract_folder

        os.makedirs(self.upload_folder, exist_ok=True)
        os.makedirs(self.extract_folder, exist_ok=True)

    def save_zip(self, uploaded_file):
        file_path = os.path.join(self.upload_folder, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return file_path

    def extract_zip(self, zip_path):
        project_name = os.path.splitext(os.path.basename(zip_path))[0]
        extract_path = os.path.join(self.extract_folder, project_name)

        os.makedirs(extract_path, exist_ok=True)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        return extract_path