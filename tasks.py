from crewai import Task
from textwrap import dedent

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class HRTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    
    def __notes_links(self):
        return "YOU WILL USE ONLY LINKS GIVEN TO YOU AND NOT WHAT YOU KNOW"

# recruiter
    def recruitment(self, agent, jobPostingURL, applicantData):
        return Task(
            description=dedent(
                f"""
                You're an experienced HR manager tasked with analyzing candidate CVs to find the best fit for a job position. 
                Your role involves extracting key details from candidate profiles to determine their qualifications, work experiences, strengths, company fit, job benefits, and overall suitability for a specific job role.
                
                Here is the web link of the job description: {jobPostingURL}
                
                Here is the information of applicants:
                {applicantData}

                For each applicant, 
                - Generate a report in Markdown format with the following sections based on each candidate skills and evaluations made
                    - Sourced candidates' profile.
                    - Reviewed job postings for position understanding.
                    - Prepared insightful interview questions.
                    - Evaluate each candidates' qualifications and work experiences.
                    - Make sure to include their name in your report
                    - Section with Passed and Failed candidates
                                       
                {self.__tip_section()}
                                       
                {self.__notes_links()}

            """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                For each applicant, 
                - Generate a report in Markdown format with the following sections based on each candidate skills and evaluations made
                    - Sourced candidates' profile.
                    - Reviewed job postings for position understanding.
                    - Prepared insightful interview questions.
                    - Evaluate each candidates' qualifications and work experiences.
                    - Make sure to include their name in your report
                    - Section with Passed and Failed candidates

            """
                ),
            output_file="reports/RecruiterReport.md"
        )

# tech
    def tech_evaluation(self, agent, jobPostingURL, candidateProfile):
        return Task(
            description=dedent(
                f"""
                Using the input from the recruiter and candidate profiles data,
                Engage in a technical interview with a candidate by asking insightful questions based on the specific technology relevant to the job at hand. 
                Evaluate the candidate's responses and knowledge of the technology as outlined in the job description, ensuring that they align with the required skill set and expertise needed for the role.
                
                Directory path containing CV:
                {candidateProfile}

                Here is the link of the job posting: {jobPostingURL}

                Generate a report based on the candidate evaluation and if candidate has good capabilities, pass to HR for further actions.

                {self.__tip_section()}

                {self.__notes_links()}
            """
            ),
            # context=[self.recruitment()],
            agent=agent,
            expected_output=dedent(
                f"""
                    Generate a report with the following sections based on the candidate skills and evaluations made
                    - Technical requirements for job postings.
                    - Insightful interview technical questions as per job requirements.
                    - Evaluated candidates' skills, qualifications and experiences.
                    - Make sure to include their name in your report
                """
            ),
            output_file="reports/TechReport.md"

        )

# hr_manager
    def finilize_contract(self, agent):
        return Task(
            description=dedent(
                f"""
                As an HR Manager/Representative, your responsibilities include finalizing the selection process for candidates who excel in technical interviews. 
                You will make the final assessment on the candidate based on the Recruiter and the technical expert evaluation reports.

                Please provide the candidate's name, the job position they applied for, their technical skills, and any specific preferences the hiring team has mentioned. 
                Additionally, include any key points from the recruiter's evaluation that are important to consider.
            
            {self.__tip_section()}
    
        """
            ),
            agent=agent,
            # context=[self.recruitment(), self.tech_evaluation()],
            expected_output=dedent(
                f"""
                    Generate a report based on the Recruiter and the technical expert evaluation reports.
                """
            ),
            output_file="reports/ManagerReport.md"

        )

# common_tasks
    # def data_extraction(self, agent, jobPostingURL, candidateProfile, companyLink, jobBenefitsLink):
    #     return Task(
    #         description=dedent(
    #             f"""
    #             You're an experienced HR manager tasked with analyzing candidate CVs to find the best fit for a job position. 
    #             Your role involves extracting key details from candidate profiles to determine their qualifications, work experiences, strengths, company fit, job benefits, and overall suitability for a specific job role.
    #             Here is the text extracted from the candidate CV:
    #             {candidateProfile}

    #             The task requires you to analyze the text extracted from a candidate CV and extract the following information:
    #             - Job Description and Qualifications: Extract the details outlining the job role and the qualifications required.
    #             - Candidate Details: Gather all relevant information about the candidate, including their name, work experiences, and strengths.
    #             - Company Information: Identify details about the company mentioned in the CV.
    #             - Job Benefits/Worklife: Look for information regarding the benefits offered by the job position and insights into the work-life balance.
    #             - Evaluation of Candidate Fit: Evaluate whether the candidate is the best fit for the position based on the extracted information.
    #             You need to delve into the text provided, interpret the data accurately, and provide a comprehensive analysis based on the requirements mentioned.
    #             For example, when analyzing candidate details, you should focus on extracting specific work experiences, strengths, and qualifications that align with the job description. This will help in determining the candidate's suitability for the position.

    #             Remember to format the report in markdown format with appropriate headings and sections for each link's analysis. The report should be well-organized and easy to read for quick reference.        
                
    #             """
    #         ),
    #         agent=agent,
    #         expected_output=dedent(
    #             f"""
                
    #             Generate a report in markdown format with appropriate headings and sections for each link's analysis. 
    #             The report should be well-organized and easy to read for quick reference.

    #             """
    #         ),
    #         output_file="report.md"
    #         # agent=agent
    #     )
    
