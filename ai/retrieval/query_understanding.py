from llm.groq_client import GroqClient

QUERY_PROMPT = """
You are an Industrial Query Routing Engine.
Analyze the user's operational question and assign it to a specialized agent.

Agent Types:
- MAINTENANCE_AGENT: For general maintenance schedules and upkeep.
- COMPLIANCE_AGENT: For safety, OISD, Factory Act, or regulatory queries.
- GENERAL_OPERATIONS_AGENT: For standard operational procedures.
- QA_SYSTEM: For strict, evidence-based technical questions and fact-checking.
- RCA_SYSTEM: For analyzing failures, breakdowns, and performing root cause analysis.

You MUST respond ONLY with a single valid JSON object following this exact schema:
{
    "Intent": "string detailing what operator wants to know",
    "AgentType": "String mapping to exactly one of the 5 Agent Types listed above",
    "Entities": ["list", "of", "machinery", "tags"],
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