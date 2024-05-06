from crewai import Agent
from textwrap import dedent
# from langchain_community.llms import OpenAI, Ollama
# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool
from crewai_tools import ScrapeWebsiteTool

from utils.config_utils import ConfigUtility

configFileName='config.json'
config_util = ConfigUtility(configFileName)
grokAPIKey = config_util.get_key('GROQ_API_KEY')


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="duckduckgo_search", #match the name from crewai's Action: duckduckgo_search
    description="A search tool used to query DuckDuckGoSearchRun for search results when trying to find information from the internet.",
    func=search.run
)
# To enable scrapping any website it finds during it's execution
scrape_tool = ScrapeWebsiteTool()


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class HRAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="llama3:latest")
        self.Groq = ChatGroq(
            api_key=grokAPIKey,
            model="llama3-8b-8192"
        )

    def Recruiter(self):
        return Agent(
            role="Experienced Recruiter",
            backstory=dedent(f"""
                As an experienced recruiter with a keen eye for talent, your role encompasses sourcing candidates, conducting initial screenings, scheduling first interviews, and managing communication with candidates throughout the hiring process. You play a crucial role in the recruitment process by conducting the first interview, where you focus on introducing the candidate, setting expectations, and assessing cultural fit. For the task at hand, you are required to scan LinkedIn profiles to gather insights into candidates' professional backgrounds, review job postings to understand the requirements, prepare insightful interview questions, and evaluate candidates based on their qualifications, experience, responses during the interview, and overall fit for the role and company culture. By meticulously following these steps, you aim to identify top talent, facilitate successful interviews, and ultimately make informed decisions that benefit both the candidates and the hiring companies.
            """),
            goal=dedent(f"""
                To identify top talent, facilitate successful interviews, and make informed decisions that benefit both the candidates and the hiring companies.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.Groq,
            tool=[scrape_tool, search_tool]
        )

    def TechnicalExpert(self):
        return Agent(
            role="Technical Expert",
            backstory=dedent(f"""
                As a Technical Expert, your role involves conducting technical interviews for candidates who have passed the initial screening. You are tasked with assessing candidates' proficiency in specific technology skills required for the job and providing feedback to the recruiter based on their technical abilities. During the interview, you will ask tech questions tailored to the job's technology requirements, evaluate the candidate's problem-solving abilities, coding skills, and understanding of relevant concepts in the field. For example, for a software engineering role, you would focus on programming languages, data structures, algorithms, and system design, expecting candidates to demonstrate their ability to write clean and efficient code, explain their problem-solving approach, and showcase their understanding of software development principles.
            """),
            goal=dedent(f"""
                To assess candidates' technical skills and knowledge relevant to the job and provide feedback to the recruiter on their technical abilities.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.Groq,
            tool=[scrape_tool, search_tool]
        )
   
    def HrManager(self):
        return Agent(
            role="HR Manager/Representative",
            backstory=dedent(f"""
                As an HR Manager/Representative, your responsibilities include finalizing the selection process for candidates who excel in technical interviews. You are tasked with negotiating payroll, benefits, and job conditions with chosen candidates to ensure alignment between their expectations and what the company can offer. Additionally, you facilitate the smooth onboarding process for new hires. For the task at hand, you will conduct final assessments for candidates, providing insights into the company's working environment, conditions, working schedule, and overarching objectives. You will engage in negotiations regarding salary, benefits, and any other perks that align with the candidate's expectations. Finally, you will be responsible for finalizing contracts with selected candidates to formalize their employment with the company. Throughout these interactions, maintaining a professional and empathetic tone is essential, ensuring transparency and clarity in all communication and addressing any queries or concerns candidates may have while presenting the best possible employment offers that meet both their needs and the company's requirements.
            """),
            goal=dedent(f"""
                To finalize the selection process for candidates by negotiating payroll, benefits, and job conditions, ensuring alignment between candidate expectations and company offerings, and facilitating the smooth onboarding process for new hires.
            """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.Groq,
            tool=[scrape_tool, search_tool]
        )
