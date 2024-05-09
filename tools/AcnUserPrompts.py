from langchain.tools import tool

class AcnUserPrompts():

  # Tool to fetch and preprocess PDF content
    @tool("Tool ask the user for inputs to clarify details based on the given questions.")
    def askUserClarification(question: str) -> str:
        """
        Tool designed to help users in various tasks by seeking clarification based on specific questions. Your task is to ask the user for inputs to clarify details based on the given questions.
        """
        print("---------------------------------------")
        print(question)
        print("---------------------------------------")

        return ""
