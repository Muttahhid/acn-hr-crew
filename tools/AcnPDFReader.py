import PyPDF2
import requests
from langchain.tools import tool
from PyPDF2 import PdfReader
import re

class AcnPDFReader():

  # Tool to fetch and preprocess PDF content
    # @tool("Tool to read PDF files from a given URL")
    # def fetch_pdf_content_url(url: str) -> str:
    #     """
    #     Fetches and preprocesses content from an ONLINE PDF.
    #     Returns the text of the PDF.
    #     """
    #     response = requests.get(url)
    #     with open('temp/temp.pdf', 'wb') as f:
    #         f.write(response.content)

    #     with open('temp/temp.pdf', 'rb') as f:
    #         pdf = PdfReader(f)
    #         text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())

    #     # Optional preprocessing of text
    #     processed_text = re.sub(r'\s+', ' ', text).strip()
    #     print(processed_text)
    #     return processed_text

    @tool("Tool to read PDF files from a path location")
    def read_pdf_file(path: str) -> str:
        """
        Fetches and preprocesses content from a PDF given its path location.
        Returns the text of the PDF.
        """
        with open(path, 'rb') as f:
            # Create a PdfReader object
            pdf = PyPDF2.PdfReader(f)

            # Extract the text from the PDF file
            text = ''
            for page in pdf.pages:
                text += page.extract_text()

        # Print the extracted text
        processed_text = re.sub(r'\s+', ' ', text).strip()
        # print(processed_text)
        return(processed_text)
    