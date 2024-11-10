import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        # Initialize ChatGroq with your API key and model
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def generate_learning_path(self, educational_background, skills, goals):
        # Define a prompt for generating a learning path based on educational background and skills
        prompt_path = PromptTemplate.from_template(
            """
            ### EDUCATIONAL BACKGROUND:
            {educational_background}

            ### SKILLS:
            {skills}

            ### GOALS:
            {goals}

            ### INSTRUCTION:
            Based on the user's educational background, skills, and specific goals, generate a personalized learning path. For each learning topic, provide the following:
            1. The topic name.
            2. A list of recommended resources categorized as:
               - **Books**: List a few books for the topic, ordered from beginner to advanced.
               - **Courses**: List a few online courses or tutorials for the topic, ordered from beginner to advanced.
               - **Blogs**: List a few blogs or articles for the topic, ordered from beginner to advanced.
            3. An estimated time for learning the topic.

            Please ensure that the output is aligned with the user's background and goals, and that resources are categorized properly.

            Structure your response in the following way:
            - **Topic**: (name of the topic)
            - **Estimated Time**: (time estimate)
            - **Books**:
              - [Book 1](URL)
              - [Book 2](URL)
            - **Courses**:
              - [Course 1](URL)
              - [Course 2](URL)
            - **Blogs**:
              - [Blog 1](URL)
              - [Blog 2](URL)
            """
        )
        # Execute the prompt with ChatGroq
        chain_path = prompt_path | self.llm
        res = chain_path.invoke(input={"educational_background": educational_background, "skills": skills, "goals": goals})
        
        # Parse JSON response
        try:
            # Directly use the model response without needing to parse into JSON
            response = res.content
        except OutputParserException:
            raise OutputParserException("Context too large or output could not be parsed.")
        
        return response

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
