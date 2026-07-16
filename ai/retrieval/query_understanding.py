from llm.groq_client import GroqClient

QUERY_PROMPT = """
You are an Industrial Query Understanding Engine.
Analyze the user's operational question and extract Intent, Entities, Time parameters, and Filters.

You MUST respond ONLY with a single valid JSON object following this exact schema layout structure:
{
    "Intent": "string detailing what operator wants to know",
    "Entities": ["list", "of", "machinery", "tags", "or", "components"],
    "Time": "any time constraint window specified or empty string",
    "Filters": {}
}
Do not include markdown headers, formatting blocks, or conversational wrapper descriptions.
"""

class QueryUnderstanding:
    def __init__(self):
        self.llm = GroqClient()

    def understand(self, question: str) -> dict:
        return self.llm.generate_json(
            prompt=question,
            system_prompt=QUERY_PROMPT
        )