from crewai import Task
from textwrap import dedent
from utils.ACN_Utility import ACN_Utility

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
                    Your role involves extracting key details from candidate profiles to determine their qualifications, work experiences, strengths and overall suitability for a specific job role.
                        Job URL: {jobPostingURL}
                        CV in PDF: {applicantData}
                        Date: {ACN_Utility.getCurrentDate("%d-%m-%Y")}
                        JSON Keys: job_description_id,candidate_id,evaluation_date,match_score,RAG_status,skills_match_required_skills,skills_match_candidate_skills,skills_match_missing_skills,experience_match_required_years,candidate_working_experiences,education_match_required_level,education_match_candidate_level,recommendations
                        JSON values datatypes: String,String,String,Decimal,String,List[String],List[String],List[String],Integer,List[String],List[String],List[String],LongText
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                   The JSON output should be according to the given schema.
                """
            ),
            output_file="reports/recruiter_"+ACN_Utility.extract_filename_from_string(applicantData)+".json"
        )

# tech
    def tech_evaluation(self, agent, jobPostingURL, applicantData):
        return Task(
            description=dedent(
                f"""
                Evaluate the candidate's experiences, knowledge of the technology as outlined in the job description, ensuring that they align with the required skill set and expertise needed for the role.
                Job URL: {jobPostingURL}
                CV in PDF: {applicantData}
                Date: {ACN_Utility.getCurrentDate("%d-%m-%Y")}

                Add these Keys to the existing JSON: tech_skills_required,tech_skills_candidate,tech_skills_missing,tools_required,tools_knowledge,tools_missing,coding_practices_required,coding_practices_candidate,coding_practices_improvement
                JSON values datatypes:List[String],List[String],List[String],List[String],List[String],List[String],List[String],List[String],List[String]
            """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                    The JSON output should be according to the given schema.
                """
            ),
            output_file="reports/tech_"+ACN_Utility.extract_filename_from_string(applicantData)+".json"

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
    def data_extraction(self, agent,applicantData, jobPostingURL):
        return Task(
            description=dedent(
                f"""
                    You're an experienced HR manager tasked with analyzing candidate CVs to find the best fit for a job position. 
                    Your role involves extracting key details from candidate profiles to determine their qualifications, work experiences, strengths and overall suitability for a specific job role.
                        Job URL: {jobPostingURL}
                        CV in PDF: {applicantData}
                        JSON Keys: job_description_id,candidate_id,match_score,isSuitable,skills_match_required_skills,skills_match_candidate_skills,skills_match_missing_skills,experience_match_required_years,experience_match_candidate_years,education_match_required_level,education_match_candidate_level,additional_criteria_required,additional_criteria_candidate,additional_criteria_missing,recommendations
                        JSON values datatypes: String,String,Decimal,Boolean,List[String],List[String],List[String],Integer,Integer,List[String],List[String],List[String],List[String],List[String],LongText
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                    The JSON output should be according to the given schema.
                """
            ),
            output_file="reports/data_extraction.json"
            # agent=agent
        )
    
