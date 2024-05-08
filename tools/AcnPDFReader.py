import requests
from langchain.tools import tool
from PyPDF2 import PdfReader
import re

class AcnPDFReader():

  # Tool to fetch and preprocess PDF content
    @tool("Tool to read PDF files from a given URL")
    def fetch_pdf_content(url: str) -> str:
        """
        Fetches and preprocesses content from a PDF given its URL.
        Returns the text of the PDF.
        """
        response = requests.get(url)
        with open('temp/temp.pdf', 'wb') as f:
            f.write(response.content)

        with open('temp/temp.pdf', 'rb') as f:
            pdf = PdfReader(f)
            text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())

        # Optional preprocessing of text
        processed_text = re.sub(r'\s+', ' ', text).strip()
        print(processed_text)
        return processed_text
