from llm.groq_client import GroqClient

class ReasoningEngine:
    def __init__(self):
        self.llm = GroqClient()

    def answer(self, prompt: str):
        return self.llm.generate(
            prompt=prompt
        )