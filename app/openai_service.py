from openai import OpenAI


class OpenaiService:
    def __init__(self):
        self.OpenAIClient = OpenAI()

    def analysis(self, resume_content, position) -> any:
        return self.OpenAIClient.chat.completions.create(
            model="gpt-4-1106-preview",
            # response_format={ "type": "json_object" },
            messages=self.generate_prompt(resume_content, position)
        )

    def generate_prompt(self, resume_content, position) -> list:

        return [
            {
                "role": "system",
                "content": """
                You are a professional engineer recruiter.
                Please Output with html tags, use h2/ul/li/etc
                """
            },
            {
                "role": "assistant",
                "content": """
                    ## Assumptions
                    - In this task, you need to use text data extracted from a PDF of a candidate's resume to determine if the candidate is the kind of person your company is looking for.
                    - The extracted text data may contain extra spaces, line breaks, special characters, etc.

                """
            },
            {
                "role": "user",
                "content": """
                    Please analyze the resume data and evaluate the degree of match with the given list of requirements.
                    Provide the following output with html tags:

                    ## Results
                    Please output ratings for each of the following items.
                    1. Resume Match Percentage: Determine and Outputs a percentage and summary of how well the resume matches the requirements overall. Determine this by considering the frequency and importance of each keyword. Give the result as a percentage.
                    - Outputs a match percentage.Percentages should be large and prominently decorated.
                    - Outputs a match percentage analysis
                    2. Resume Summary: Summarize the key details and qualifications from the resume.Keep it as short as possible.
                    3. Pros & Cons Evaluation: Evaluate the strengths and weaknesses of this candidate based on their resume data.
                    4. Questions to ask if you are interviewing. please provide three candidates.
                """
            },
            {
                "role": "user",
                "content": """
                    This is requirements for responsibilities:
                    {}
                """.format(position.requirements_responsibilities)
            },
            {
                "role": "user",
                "content": """
                    This is requirements for skills:
                    {}
                """.format(position.requirements_skills)
            },
            {
                "role": "user",
                "content": """
                    Please run the analysis and generate the requested outputs based on the text data described in the following message. Thank you!
                """
            },
            {
                "role": "user",
                "content": """
                    {}
                """.format(resume_content)
            }
        ]
