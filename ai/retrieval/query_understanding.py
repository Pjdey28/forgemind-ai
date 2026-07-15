from llm.groq_client import GroqClient
from llm.output_parser import OutputParser


QUERY_PROMPT = """
You are an Industrial Query Understanding Engine.

Extract

Intent

Entities

Time

Filters

Return JSON only.
"""


class QueryUnderstanding:

    def __init__(self):

        self.llm = GroqClient()

    def understand(self, question):

        response = self.llm.generate(

            prompt=question,

            system_prompt=QUERY_PROMPT

        )

        return OutputParser.parse_json(response)