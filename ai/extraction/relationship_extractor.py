from llm.groq_client import GroqClient
from extraction.prompts import RELATIONSHIP_EXTRACTION_PROMPT
from extraction.extraction_result import ExtractedRelationship

class RelationshipExtractor:
    def __init__(self):
        self.llm = GroqClient()

    def extract(self, chunk, valid_ids):
        # Inject the valid IDs into the prompt so the LLM knows what to connect
        entity_str = ", ".join(valid_ids) if valid_ids else "None provided"
        formatted_prompt = RELATIONSHIP_EXTRACTION_PROMPT.replace("{entity_list}", entity_str)
        result = self.llm.generate_json(
            prompt=chunk.text,
            system_prompt=formatted_prompt
        )

        relationships = []
        
        if isinstance(result, dict):
            result = result.get("relationships", [result])
        elif not isinstance(result, list):
            result = []

        for relation in result:
            if isinstance(relation, dict) and "source" in relation and "relation" in relation and "target" in relation:
                # Ensure the LLM actually used a valid ID before appending
                source_id = str(relation["source"]).strip().upper()
                target_id = str(relation["target"]).strip().upper()
                
                if source_id in valid_ids and target_id in valid_ids:
                    relationships.append(
                        ExtractedRelationship(
                            source=source_id,
                            relation=str(relation["relation"]).strip().upper().replace(" ", "_"),
                            target=target_id,
                            properties=relation.get("properties", {})
                        )
                    )

        return relationships