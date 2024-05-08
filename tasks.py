from crewai import Task
from textwrap import dedent

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class HRTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

# hr_manager
    def finilize_contract(self, agent):
        return Task(
            description=dedent(
                f"""
            Using the input from the recruiter and the tech expert and data from the web links retrieved,
            Conduct final assessments for candidates to assess their suitability for the roles they have applied for. 
            During this process, provide them with insights into the company's working environment, conditions, working schedule, and overarching objectives. Following this, you will engage in negotiations regarding salary, benefits, and any other perks that align with the candidate's expectations. 
            Finally, finalize the contracts with the selected candidates to formalize their employment with the company.
            Maintain a professional and empathetic tone throughout the interactions with the candidates, ensuring transparency and clarity in all communication. 
            Be prepared to address any queries or concerns candidates may have while presenting the best possible employment offers that meet both their needs and the company's requirements.
            
            {self.__tip_section()}
    
        """
            ),
            agent=agent,
            human_input=True,
            # context=[self.recruitment(), self.tech_evaluation()],
            expected_output=dedent(
                f"""
            Conducted final candidate assessments.
            Provided insights into company culture and objectives.
            Negotiated salary, benefits, and perks.
            Finalized contracts and ensured transparency.
            Addressed candidate queries and concerns.
    
        """
            )
        )

# recruiter
    def recruitment(self, agent):
        return Task(
            description=dedent(
                f"""
            Using data from the web links retrieved, 
            Act as first point of contact for the candidate during the interview process.
            Guide through the recruitment process. 
            Sourcing candidates, conducting initial screenings, and scheduling first interviews. 
            Focus should be on introducing the candidate to the role, understanding their expectations, and evaluating their fit within the company culture. 
            Managing communication with candidates at every stage of the hiring process.
            Scanning their LinkedIn profile to gather insights
            Reviewing the job posting to understand the requirements, preparing relevant questions to ask during the interview, and evaluating the candidate based on their responses, qualifications, and overall suitability for the role
            Handle to the tech expert for shortlisted candidates.
            Termiate/Conclude the interview process based on reports from other agents.
            Make sure to include their name and portfolio link in your report
                                       
            {self.__tip_section()}

        """
            ),
            agent=agent,
            human_input=True,
            expected_output=dedent(
                f"""
                Sourced candidates' profiles.
                Reviewed job postings for position understanding.
                Prepared insightful interview questions.
                Conducted first interviews, assessing cultural fit.
                Evaluated candidates' qualifications and experiences.
                Make sure to include their name and portfolio link in your report
        
            """
                )
        )

# tech
    def tech_evaluation(self, agent):
        return Task(
            description=dedent(
                f"""
            Using the input from the recruiter and data from the web links retrieved,
            Engage in a technical interview with a candidate by asking insightful questions based on the specific technology relevant to the job at hand. 
            Evaluate the candidate's responses and knowledge of the technology as outlined in the job description, ensuring that they align with the required skill set and expertise needed for the role.
            Generate a report based on the candidate evaluation and if candidate has good capabilities, pass to the HR manager for further actions.
            Make sure to include their name and portfolio link in your report

            {self.__tip_section()}
       """
            ),
            # context=[self.recruitment()],
            agent=agent,
            human_input=True,
            expected_output=dedent(
                f"""
                Conducted final candidate assessments.
                Provided insights into company culture and objectives.
                Negotiated salary, benefits, and perks.
                Finalized contracts and ensured transparency.
                Addressed candidate queries and concerns.
                Make sure to include their name and linkedin link in your report

                """
            )
        )

# common_tasks
    def data_extraction(self, agent, jobPostingURL, candidateProfile, companyLink, jobBenefitsLink):
        return Task(
            description=dedent(
                f"""
                You are an advanced information retrieval system that specializes in extracting specific content from websites and documents on a variety of topics or subjects.
                Your task is to fetch the content from websites and documents based on the provided parameters.
                Use the AcnPDFReader tool in preference to fetch information

                Here are the details you need to keep in mind:
                
                First, retrieve content from the following links/documents:
                - Candidate CV: {candidateProfile}

                Remember to format the report in markdown format with appropriate headings and sections for each link's analysis. The report should be well-organized and easy to read for quick reference.        
                
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                
                Generate a report in markdown format with appropriate headings and sections for each link's analysis. 
                The report should be well-organized and easy to read for quick reference.

                """
            ),
            output_file="report.md"
            # agent=agent
        )
