from llm.groq_client import GroqClient
from retrieval.prompt_builder import PromptBuilder

class ReasoningEngine:
    def __init__(self):
        self.llm = GroqClient()

    def answer(self, prompt: str):
        # Pass both the context prompt and the strict System Persona to Groq
        return self.llm.generate(
            prompt=prompt,
            system_prompt=PromptBuilder.SYSTEM_PROMPT
        )