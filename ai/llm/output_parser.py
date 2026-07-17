import json
import re
from llm.exceptions import LLMResponseException

class OutputParser:
    @staticmethod
    def parse_json(text: str):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Fallback regex helper matching structural JSON brackets
            json_match = re.search(r"(\{.*\}|\[.*\])", text, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(1))
                except json.JSONDecodeError:
                    pass
            raise LLMResponseException(f"Failed to parse JSON: {text}")