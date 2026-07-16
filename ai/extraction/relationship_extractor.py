from llm.groq_client import GroqClient

from extraction.prompts import RELATIONSHIP_EXTRACTION_PROMPT

from extraction.extraction_result import ExtractedRelationship


class RelationshipExtractor:

    def __init__(self):

        self.llm = GroqClient()

    def extract(

        self,

        chunk

    ):

        result = self.llm.generate_json(

            prompt=chunk.text,

            system_prompt=RELATIONSHIP_EXTRACTION_PROMPT

        )

        relationships = []

        for relation in result:

            relationships.append(

                ExtractedRelationship(

                    source=relation["source"],

                    relation=relation["relation"],

                    target=relation["target"],

                    properties=relation.get(

                        "properties",

                        {}

                    )

                )

            )

        return relationships