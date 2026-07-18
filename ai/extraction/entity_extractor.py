from llm.groq_client import GroqClient
from extraction.prompts import ENTITY_EXTRACTION_PROMPT
from extraction.extraction_result import ExtractedEntity

class EntityExtractor:
    def __init__(self):
        self.llm = GroqClient()

    def extract(self, chunk):
        # Fixed: Read chunk.text instead of non-existent chunk.content
        result = self.llm.generate_json(
            prompt=chunk.text,
            system_prompt=ENTITY_EXTRACTION_PROMPT
        )
        entities = []
        if isinstance(result, dict):
            for label, values in result.items():
                if isinstance(values, list):
                    for value in values:
                        if isinstance(value, dict):
                            entities.append(
                                ExtractedEntity(
                                    id=str(value.get("id", value.get("name", ""))),
                                    label=label,
                                    properties=value
                                )
                            )
        return entities