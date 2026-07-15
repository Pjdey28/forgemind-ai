from llm.groq_client import GroqClient

from extraction.prompts import ENTITY_EXTRACTION_PROMPT

from extraction.extraction_result import ExtractedEntity


class EntityExtractor:

    def __init__(self):

        self.llm = GroqClient()

    def extract(

        self,

        chunk

    ):

        result = self.llm.generate_json(

            prompt=chunk.content,

            system_prompt=ENTITY_EXTRACTION_PROMPT

        )

        entities = []

        for label, values in result.items():

            for value in values:

                entities.append(

                    ExtractedEntity(

                        id=value.get(

                            "id",

                            value.get(

                                "name"

                            )

                        ),

                        label=label,

                        properties=value

                    )

                )

        return entities