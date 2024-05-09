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
    def recruitment(self, agent, jobPostingURL, candidateProfile):
        return Task(
            description=dedent(
                f"""
                You're an experienced HR manager tasked with analyzing candidate CVs to find the best fit for a job position. 
                Your role involves extracting key details from candidate profiles to determine their qualifications, work experiences, strengths, company fit, job benefits, and overall suitability for a specific job role.
                
                Here is the text extracted from the candidate CV:
                {candidateProfile}

                Here is the link of the job posting: {jobPostingURL}
                                       
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
                ),
            output_file="HRreport.md"
        )

# tech
    def tech_evaluation(self, agent, jobPostingURL, candidateProfile):
        return Task(
            description=dedent(
                f"""
                Using the input from the recruiter and candidate profiles data,
                Engage in a technical interview with a candidate by asking insightful questions based on the specific technology relevant to the job at hand. 
                Evaluate the candidate's responses and knowledge of the technology as outlined in the job description, ensuring that they align with the required skill set and expertise needed for the role.
                
                Here is the candidate CV:
                {candidateProfile}

                Here is the link of the job posting: {jobPostingURL}

                Generate a report based on the candidate evaluation and if candidate has good capabilities, pass to HR for further actions.

            {self.__tip_section()}
       """
            ),
            # context=[self.recruitment()],
            agent=agent,
            human_input=True,
            expected_output=dedent(
                f"""
                    Generate a report based on the candidate evaluation and if candidate has good capabilities, pass to HR for further actions.
                """
            ),
            output_file="Techreport.md"

        )

# common_tasks
    def data_extraction(self, agent, jobPostingURL, candidateProfile, companyLink, jobBenefitsLink):
        return Task(
            description=dedent(
                f"""
                You're an experienced HR manager tasked with analyzing candidate CVs to find the best fit for a job position. 
                Your role involves extracting key details from candidate profiles to determine their qualifications, work experiences, strengths, company fit, job benefits, and overall suitability for a specific job role.
                Here is the text extracted from the candidate CV:
                {candidateProfile}

                The task requires you to analyze the text extracted from a candidate CV and extract the following information:
                - Job Description and Qualifications: Extract the details outlining the job role and the qualifications required.
                - Candidate Details: Gather all relevant information about the candidate, including their name, work experiences, and strengths.
                - Company Information: Identify details about the company mentioned in the CV.
                - Job Benefits/Worklife: Look for information regarding the benefits offered by the job position and insights into the work-life balance.
                - Evaluation of Candidate Fit: Evaluate whether the candidate is the best fit for the position based on the extracted information.
                You need to delve into the text provided, interpret the data accurately, and provide a comprehensive analysis based on the requirements mentioned.
                For example, when analyzing candidate details, you should focus on extracting specific work experiences, strengths, and qualifications that align with the job description. This will help in determining the candidate's suitability for the position.

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
    
