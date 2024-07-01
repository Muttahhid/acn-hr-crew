import os
from crewai import Agent
from textwrap import dedent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
# from langchain_community.llms import Ollama
# from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool
from crewai_tools import PDFSearchTool, FileReadTool

from tools.AcnPDFReader import AcnPDFReader
from tools.AcnWebScraper import AcnWebScraper

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = os.getenv('LLM_MODEL')

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class HRAgents:
    def __init__(self, applicantData):

        # self.LLM = Ollama(model="llama3:latest")
        # self.LLM = ChatOpenAI(
        #     model = "llama3_techverse",
        #     base_url = "http://localhost:11434/v1"
        # )
        self.LLM = ChatGroq(
            api_key=GROQ_API_KEY,
            model=LLM_MODEL
        )   

        self.scrape_tool = AcnWebScraper.extract_web_content
        # self.file_read_tool = FileReadTool(
        #     file_path='json_template.json',
        #     description='A tool to read the output example file.'
        # )

        self.pdf_scrape_tool = AcnPDFReader.read_pdf_file

        # self.pdf_scrape_tool = PDFSearchTool(
            # pdf=applicantData,
            # config=dict(
            #     llm=dict(
            #         provider="groq", # 'openai', 'azure_openai', 'anthropic', 'huggingface', 'cohere', 'together', 'gpt4all', 'ollama', 'jina', 'llama2', 'vertexai', 'google', 'aws_bedrock', 'mistralai', 'vllm', 'groq', 'nvidia'
            #         config=dict(
            #             model=LLM_MODEL,
            #             # temperature=0.5,
            #             # top_p=1,
            #             # stream=true,
            #         ),
            #     )
                # embedder=dict(
                #     provider="gpt4all", # or openai, ollama, ...
                #     config=dict(
                #         model="all-MiniLM-L6-v2.gguf2.f16.gguf"
                #         # task_type="retrieval_document",
                #         # title="Embeddings",
                #     ),
                # ),
            # )
        # )

    def Recruiter(self):
        return Agent(
            role="Experienced Recruiter",
            backstory=dedent(f"""
                You are a professional Recruiter who matches qualified individuals with specific open positions at an organization.
            """),
            goal=dedent(f"""
                To identify top talent and make informed decisions that benefit both the candidates and the hiring companies to match their skill sets and requirements.
            """),
            verbose=True,
            llm=self.LLM,
            tools=[self.scrape_tool, self.pdf_scrape_tool]
        )

    def TechnicalExpert(self):
        return Agent(
            role="Technical Expert",
            backstory=dedent(f"""
                As a technical expert in the hiring process, you are someone who handles sourcing, screening, interviewing, and selecting candidates for technical roles within an organization. 
                You will assess candidates technical skills, experience, and qualifications to ensure a good fit for specific technical positions
            """),
            goal=dedent(f"""
                To assess candidates' technical skills and knowledge relevant to the job and provide feedback to the recruiter on their technical abilities.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.LLM,
            # tools=[self.scrape_tool]
        )
   
    def HrManager(self):
        return Agent(
            role="HR Manager/Representative",
            backstory=dedent(f"""
                As an HR Manager/Representative, your responsibilities include finalizing the selection process for candidates who excel in technical interviews.
                You will make the final assessment on the candidate based on the Recruiter and the technical evaluation reports.
            """),
            goal=dedent(f"""
                To finalize the selection process for candidates by negotiating payroll, benefits, and job conditions, ensuring alignment between candidate expectations and company offerings, and facilitating the smooth onboarding process for new hires.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.LLM,
            tools=[self.scrape_tool]
        )
   
    def DigitalAgent(self):

        return Agent(
            role="Data Analyst",
            backstory=dedent(f"""
                You are a professional data analyst who excels in extracting and processing information from various file formats and web links.
            """),
            goal=dedent(f"""
                Converting PDF documents and web links into structured data formats like JSON.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.LLM,
            tools=[self.scrape_tool, self.pdf_scrape_tool]
        )
    