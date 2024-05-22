import os
from crewai import Crew, Process
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama

from agents import HRAgents
from tasks import HRTasks

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL')

class HRCrew:
    def __init__(self,jobPostingURL, candidateProfile):
        self.jobPostingURL = jobPostingURL
        self.candidateProfile = candidateProfile

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = HRAgents(self.jobPostingURL, self.candidateProfile)
        tasks = HRTasks()

        # Define your custom agcents and tasks here
        recruiter = agents.Recruiter()
        tech_expert = agents.TechnicalExpert()

        # hr_manager = agents.HrManager()
        # digital_agent = agents.DigitalAgent(self.candidateProfile)

        # Custom tasks include agent name and variables as input
        recruitment = tasks.recruitment(
            recruiter,
            self.jobPostingURL,
            self.candidateProfile
        )

        tech_evaluation = tasks.tech_evaluation(
            tech_expert,
            self.jobPostingURL,
            self.candidateProfile
        )

        # finilize_contract = tasks.finilize_contract(
        #     hr_manager
        # )

        # data_extraction = tasks.data_extraction(
        #     digital_agent,
        #     self.jobPostingURL,
        #     self.candidateProfile,
        #     config_util.get_key('companyURL'),
        #     config_util.get_key('benefitsURL')
        # )

        # Define your custom crew here
        crew = Crew(
            agents=[recruiter, tech_expert],
            tasks=[recruitment, tech_evaluation],
            verbose=True,
            # process=Process.sequential
            process=Process.hierarchical,
            manager_llm=ChatGroq(
                api_key=GROQ_API_KEY,
                model=LLM_MODEL
            )
        )

        result = crew.kickoff()
        return result

