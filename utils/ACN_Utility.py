import re
from datetime import datetime

class ACN_Utility:
    def extract_filename_from_string(file_path):
        # Using regular expression to find the filename
        match = re.search(r'/([^/]+)\.pdf$', file_path)
        if match:
            return match.group(1)  # Group 1 contains the filename without extension
        else:
            return None  # Return None if no match found
        
    def getCurrentDate(format):
        current_date = datetime.now()
        formatted_date = current_date.strftime(format)
        return formatted_date