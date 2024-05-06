import os
import json
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
# from decouple import config

from textwrap import dedent
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
    def __init__(self,jobPostingURL, linkedinURL):
        self.jobPostingURL = jobPostingURL
        self.linkedinURL = linkedinURL

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = HRAgents()
        tasks = HRTasks()

        # Define your custom agents and tasks here
        recruiter = agents.Recruiter()
        tech_expert = agents.TechnicalExpert()
        hr_manager = agents.HrManager()

        # Custom tasks include agent name and variables as input
        recruitment = tasks.recruitment(
            recruiter
        )

        tech_evaluation = tasks.tech_evaluation(
            tech_expert
        )

        finilize_contract = tasks.finilize_contract(
            hr_manager
        )

        get_job_description = tasks.get_job_description(
            jobPostingURL,
            linkedinURL,
            config_util.get_key('companyURL'),
            config_util.get_key('benefitsURL')
        )

        # Define your custom crew here
        crew = Crew(
            agents=[recruiter, tech_expert, hr_manager],
            tasks=[get_job_description, recruitment, tech_evaluation, finilize_contract],
            verbose=True,
            process=Process.hierarchical,
            manager_llm=ChatGroq(
            api_key=grokAPIKey,
            model="llama3-8b-8192"
        )
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to HR Crew AI")
    print("-------------------------------")
    # jobPostingURL = input(dedent("""Job Posting URL: """))
    # linkedinURL = input(dedent("""Candidate Linkedin URL: """))
    jobPostingURL = "https://www.accenture.com/gb-en/careers/jobdetails?id=R00181431_en&title=Java+Developer+-+Newcastle&c=car_glb_curateddailycondialogbox_12220771&n=otc_0621"
    linkedinURL = "https://www.linkedin.com/in/muttahhid-jomeer/"

    print("job: ", jobPostingURL)
    print("Linkedin: ", linkedinURL)

    acn_hr_crew = HRCrew(jobPostingURL,linkedinURL)
    result = acn_hr_crew.run()
    print("\n\n########################")
    print("## Here is you run result:")
    print("########################\n")
    print(result)
