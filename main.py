from HRCrew import HRCrew
from tools.AcnPDFReader import AcnPDFReader
import pathlib

jobPostingURL = "https://www.accenture.com/mu-en/careers/jobdetails?id=R00176183_en"
# linkedinURL = "https://adouti.com/wordpress/wp-content/uploads/2021/02/MiguelMresume-1.pdf"
# linkedinURL = "https://www.dayjob.com/downloads/CV_examples/java_developer_cv_template.pdf"
# linkedinURL = "https://www.avinashmeetoo.com/other/cv/20240506-avinash-meetoo-cv.pdf"
linkedinURL = "pdf/20240506-avinash-meetoo-cv.pdf"

def pdf2txt(linkedinURL):

    # txtFilename = 'txt/' + get_filename_from_url(linkedinURL) + '.txt'
    content = AcnPDFReader.fetch_pdf_content(linkedinURL)
    # write_string_to_file(content, txtFilename)
    return content


def get_filename_from_url(url):
    path = pathlib.Path(url)
    return path.name.split('.')[0]

def write_string_to_file(string, filename):
    with open(filename, 'w') as f:
        f.write(string)

def initCrew(jobPostingURL, candidateProfile):
    
    print("## Welcome to HR Crew AI")
    print("-------------------------------")

    print("Job Posting: ", jobPostingURL)
    print("Candidate Portfolio: ", candidateProfile)

    acn_hr_crew = HRCrew(jobPostingURL, candidateProfile)
    result = acn_hr_crew.run()

    print("\n\n########################")
    print("## Here is you run result:")
    print("########################\n")
    print(result)

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    # generate_cv_txt = pdf2txt(linkedinURL)
    initCrew(jobPostingURL, linkedinURL)