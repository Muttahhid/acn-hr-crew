import json
from typing import List, Dict, Any

class JobEvaluation:
    class SkillsMatch:
        def __init__(self, required_skills: List[str] = None, candidate_skills: List[str] = None, missing_skills: List[str] = None):
            self.required_skills = required_skills if required_skills is not None else []
            self.candidate_skills = candidate_skills if candidate_skills is not None else []
            self.missing_skills = missing_skills if missing_skills is not None else []

        def to_dict(self) -> Dict[str, Any]:
            return {
                "required_skills": self.required_skills,
                "candidate_skills": self.candidate_skills,
                "missing_skills": self.missing_skills
            }

    class ExperienceMatch:
        def __init__(self, required_experience_years: float = 0, candidate_experience_years: float = 0):
            self.required_experience_years = required_experience_years
            self.candidate_experience_years = candidate_experience_years

        def to_dict(self) -> Dict[str, Any]:
            return {
                "required_experience_years": self.required_experience_years,
                "candidate_experience_years": self.candidate_experience_years
            }

    class EducationMatch:
        def __init__(self, required_education_level: str = "", candidate_education_level: str = ""):
            self.required_education_level = required_education_level
            self.candidate_education_level = candidate_education_level

        def to_dict(self) -> Dict[str, Any]:
            return {
                "required_education_level": self.required_education_level,
                "candidate_education_level": self.candidate_education_level
            }

    class AdditionalCriteria:
        def __init__(self, required_criteria: List[str] = None, candidate_criteria: List[str] = None, missing_criteria: List[str] = None):
            self.required_criteria = required_criteria if required_criteria is not None else []
            self.candidate_criteria = candidate_criteria if candidate_criteria is not None else []
            self.missing_criteria = missing_criteria if missing_criteria is not None else []

        def to_dict(self) -> Dict[str, Any]:
            return {
                "required_criteria": self.required_criteria,
                "candidate_criteria": self.candidate_criteria,
                "missing_criteria": self.missing_criteria
            }

    class Details:
        def __init__(self, skills_match: 'JobEvaluation.SkillsMatch' = None, experience_match: 'JobEvaluation.ExperienceMatch' = None, education_match: 'JobEvaluation.EducationMatch' = None, additional_criteria: 'JobEvaluation.AdditionalCriteria' = None):
            self.skills_match = skills_match if skills_match is not None else JobEvaluation.SkillsMatch()
            self.experience_match = experience_match if experience_match is not None else JobEvaluation.ExperienceMatch()
            self.education_match = education_match if education_match is not None else JobEvaluation.EducationMatch()
            self.additional_criteria = additional_criteria if additional_criteria is not None else JobEvaluation.AdditionalCriteria()

        def to_dict(self) -> Dict[str, Any]:
            return {
                "skills_match": self.skills_match.to_dict(),
                "experience_match": self.experience_match.to_dict(),
                "education_match": self.education_match.to_dict(),
                "additional_criteria": self.additional_criteria.to_dict()
            }

    def __init__(self, job_description_id: str = "", candidate_id: str = "", evaluation_date: str = "", match_score: float = 0.0, suitability: bool = False, details: 'JobEvaluation.Details' = None, recommendations: List[str] = None):
        self.job_description_id = job_description_id
        self.candidate_id = candidate_id
        self.evaluation_date = evaluation_date
        self.match_score = match_score
        self.suitability = suitability
        self.details = details if details is not None else JobEvaluation.Details()
        self.recommendations = recommendations if recommendations is not None else []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "job_description_id": self.job_description_id,
            "candidate_id": self.candidate_id,
            "evaluation_date": self.evaluation_date,
            "match_score": self.match_score,
            "suitability": self.suitability,
            "details": self.details.to_dict(),
            "recommendations": self.recommendations
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)