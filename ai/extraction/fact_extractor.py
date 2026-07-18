from llm.groq_client import GroqClient
from extraction.prompts import FACT_EXTRACTION_PROMPT
from extraction.extraction_result import ExtractedFact

class FactExtractor:

    def __init__(self):
        self.llm = GroqClient()

    def extract(self, chunk):
        # We ensure chunk.text is used as fixed earlier
        result = self.llm.generate_json(
            prompt=chunk.text,
            system_prompt=FACT_EXTRACTION_PROMPT
        )

        facts = []
        
        # Safety net: Ensure the result is a list
        if isinstance(result, dict):
            # If the LLM wraps it in a dict like {"facts": [...]}, try to extract it
            result = result.get("facts", [result])
        elif not isinstance(result, list):
            result = []

        # Safely loop through and validate keys
        for item in result:
            if isinstance(item, dict) and "key" in item and "value" in item:
                facts.append(
                    ExtractedFact(
                        key=str(item["key"]),
                        value=item["value"],
                        confidence=item.get("confidence", 1.0)
                    )
                )

        return facts