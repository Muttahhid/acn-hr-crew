import os
import PyPDF2
from HRCrew import HRCrew
from tools.AcnPDFReader import AcnPDFReader

jobPostingURL = "https://www.accenture.com/mu-en/careers/jobdetails?id=R00148588_en"
candidateProfile = "pdf/Deni_Begaj.pdf"
directory = "./pdf"
output = "./output.txt"

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def list_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def read_dir_pdf(directory, output):
    for i, file in enumerate(list_directory(directory)):
        if file.endswith('.pdf'):
            pdf_file = os.path.join(directory, file)
           
            text = AcnPDFReader.read_pdf_file(pdf_file)
            with open(f"{output}", 'a', encoding='utf-8') as f:
                # print(text)
                f.write(text)
                f.write("---------------------END_OF_CANDIDATE_" + str(i+1) + "_DATA---------------------\n")
                f.write("\n")

def read_text_from_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text

def initCrew(jobPostingURL, applicantData):
    
    print("## Welcome to HR Crew AI")
    print("-------------------------------")

    print("Job Posting: ", jobPostingURL)
    print("applicantData: ", applicantData)

    acn_hr_crew = HRCrew(jobPostingURL, applicantData)
    result = acn_hr_crew.run()

    print("\n\n########################")
    print("## Here is you run result:")
    print("########################\n")
    print(result)

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":

    # delete_file(output)
    # read_dir_pdf(directory, output)

    # for i, file in enumerate(list_directory(directory)):
    #     if file.endswith('.pdf'):
    #         pdf_file = os.path.join(directory, file)
           
    #         print("Current PDF => ", pdf_file)
    #         # text = AcnPDFReader.read_pdf_file(pdf_file)
    #         initCrew(jobPostingURL, pdf_file)
    initCrew(jobPostingURL, candidateProfile)