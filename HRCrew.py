from crewai import Crew, Process
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama

from agents import HRAgents
from tasks import HRTasks
from utils.config_utils import ConfigUtility

configFileName='config.json'
config_util = ConfigUtility(configFileName)
grokAPIKey = config_util.get_key('GROQ_API_KEY')

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class HRCrew:
    def __init__(self,jobPostingURL, candidateProfile):
        self.jobPostingURL = jobPostingURL
        self.candidateProfile = candidateProfile

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = HRAgents()
        tasks = HRTasks()

        # Define your custom agcents and tasks here
        recruiter = agents.Recruiter(
            self.jobPostingURL,
            self.candidateProfile
        )
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
            # agents=[recruiter, tech_expert, hr_manager],
            # tasks=[recruitment, tech_evaluation, finilize_contract],
            agents=[recruiter, tech_expert],
            tasks=[recruitment, tech_evaluation],
            verbose=True,
            process=Process.sequential
            # process=Process.hierarchical,
            # manager_llm=ChatGroq(
            #     api_key=grokAPIKey,
            #     model="llama3-8b-8192"
            # )
        )

        result = crew.kickoff()
        return result

