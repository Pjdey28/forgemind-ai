from extraction.entity_extractor import EntityExtractor
from extraction.relationship_extractor import RelationshipExtractor
from extraction.fact_extractor import FactExtractor
from extraction.extraction_result import ExtractionResult

class IndustrialExtractor:
    def __init__(self):
        self.entities = EntityExtractor()
        self.relationships = RelationshipExtractor()
        self.facts = FactExtractor()

    def extract(self, chunk):
        # 1. Extract Entities First
        extracted_entities = self.entities.extract(chunk)
        
        # 2. Harvest the IDs to use as a strict constraint
        valid_ids = [str(entity.id).strip().upper() for entity in extracted_entities]

        # 3. Pass valid IDs to Relationships (Facts usually don't need strict entity mapping)
        extracted_relationships = self.relationships.extract(chunk, valid_ids)
        extracted_facts = self.facts.extract(chunk)

        return ExtractionResult(
            entities=extracted_entities,
            relationships=extracted_relationships,
            facts=extracted_facts
        )