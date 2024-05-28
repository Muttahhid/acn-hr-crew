import os
from crewai import Agent
from textwrap import dedent
# from langchain_community.llms import OpenAI, Ollama
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
# from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool
from crewai_tools import ScrapeWebsiteTool, PDFSearchTool, DirectoryReadTool

from tools.AcnPDFReader import AcnPDFReader
from tools.AcnUserPrompts import AcnUserPrompts
from tools.AcnWebScraper import AcnWebScraper
from utils.config_utils import ConfigUtility


load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL')

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class HRAgents:
    def __init__(self, jobPostingURL, candidateProfile):

        # self.LLM = Ollama(model="llama3:latest")
        self.LLM = ChatGroq(
            api_key=GROQ_API_KEY,
            model=LLM_MODEL
        )
        # self.scrape_tool = ScrapeWebsiteTool(
        #     url=jobPostingURL
        # )
        self.scrape_tool = AcnWebScraper.fetch_web_content
        self.list_dir = DirectoryReadTool(directory=candidateProfile)
        self.pdf_scrape_tool = PDFSearchTool(
            # pdf=candidateProfile,
            config=dict(
                llm=dict(
                    provider="groq", # 'openai', 'azure_openai', 'anthropic', 'huggingface', 'cohere', 'together', 'gpt4all', 'ollama', 'jina', 'llama2', 'vertexai', 'google', 'aws_bedrock', 'mistralai', 'vllm', 'groq', 'nvidia'
                    config=dict(
                        model=LLM_MODEL,
                        # temperature=0.5,
                        # top_p=1,
                        # stream=true,
                    ),
                ),
                embedder=dict(
                    provider="gpt4all", # or openai, ollama, ...
                    config=dict(
                        model="all-MiniLM-L6-v2.gguf2.f16.gguf"
                        # task_type="retrieval_document",
                        # title="Embeddings",
                    ),
                ),
            )
        )

    def Recruiter(self):
        return Agent(
            role="Experienced Recruiter",
            backstory=dedent(f"""
                You are a professional Recruiter who matches qualified individuals with specific open positions at an organization.
                For the task at hand, you are required to analyse candidate profiles to gather insights into candidates' professional backgrounds, review job postings to understand the requirements, prepare insightful interview questions, and evaluate candidates based on their qualifications, experience, responses during the interview, and overall fit for the role. 

            """),
            goal=dedent(f"""
                To identify top talent and make informed decisions that benefit both the candidates and the hiring companies to match their skill sets and requirements.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.LLM,
            tools=[self.scrape_tool,self.list_dir, self.pdf_scrape_tool]
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
            tools=[self.scrape_tool, self.list_dir, self.pdf_scrape_tool]
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
            tool=[self.scrape_tool, self.list_dir, self.pdf_scrape_tool]
        )
   
    # def DigitalAgent(self, candidateProfile):

    #     return Agent(
    #         role="Digital Agent",
    #         backstory=dedent(f"""
    #            You're an experienced HR manager tasked with analyzing candidate CVs to find the best fit for a job position. 
    #             Your role involves extracting key details from candidate profiles to determine their qualifications, work experiences, strengths, company fit, job benefits, and overall suitability for a specific job role.
    #             Here is the text extracted from the candidate CV:
    #             {candidateProfile}
    #         """),
    #         goal=dedent(f"""
    #             Remember to focus on accuracy, relevancy, and ensuring that the extracted content aligns with the given parameters. 
    #             Ensure that the content is presented in a clear and concise manner for easy comprehension.
                        
    #             Format the report in markdown format with appropriate headings and sections for each link's analysis. The report should be well-organized and easy to read for quick reference.
    #         """),
    #         # tools=[tool_1, tool_2],
    #         allow_delegation=False,
    #         verbose=True,
    #         llm=self.Groq,
    #         tools=[]
    #     )
    