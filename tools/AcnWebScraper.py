import requests
from langchain.tools import tool
from bs4 import BeautifulSoup

class AcnWebScraper():

    # Tool to fetch and preprocess web text
    @tool("Tool to extract text from a given URL")
    def fetch_web_content(url: str) -> str:
        """
        Fetches and preprocesses text from a webpage given its URL.
        Returns the text of the webpage.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Assuming the job details are in a specific HTML element (e.g., <div class="job-listing-details">)
        job_description = soup.find("div", class_="job-listing-details").get_text()

        lines = job_description.split("\n")  # Split the text into lines

        # Filter out empty lines and lines with minimal content (e.g., whitespace)
        filtered_lines = [line.strip() for line in lines if line.strip()]

        # Join the filtered lines back into a single string
        cleaned_text = "\n".join(filtered_lines)
        return cleaned_text
        
    
# url= "https://www.accenture.com/mu-en/careers/jobdetails?id=R00176185_en&title=Front-End%20Angular%20%2FReactJS%20Developer"
# ws = AcnWebScraper.fetch_web_content(url)
# print(ws)