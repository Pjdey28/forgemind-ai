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

        return ExtractionResult(

            entities=self.entities.extract(chunk),

            relationships=self.relationships.extract(chunk),

            facts=self.facts.extract(chunk)

        )