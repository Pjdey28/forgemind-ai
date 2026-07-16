import json
import re
from groq import Groq
from config.settings import settings
from llm.exceptions import LLMResponseException

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.MODEL_NAME

    def generate(self, prompt: str, system_prompt: str | None = None, temperature: float = 0.2) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=settings.MAX_TOKENS
        )
        return response.choices[0].message.content

    def generate_json(self, prompt: str, system_prompt: str) -> dict | list:
        raw_response = self.generate(prompt, system_prompt, temperature=0.0)
        try:
            return json.loads(raw_response)
        except json.JSONDecodeError:
            # Fallback regex helper matching structural JSON brackets if LLM provides conversational markdown wrapping
            json_match = re.search(r"(\{.*\}|\[.*\])", raw_response, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(1))
                except json.JSONDecodeError:
                    pass
            raise LLMResponseException(f"Failed to parse clean structural JSON from Groq layout block: {raw_response}")