from llm.groq_client import GroqClient

from extraction.prompts import FACT_EXTRACTION_PROMPT

from extraction.extraction_result import ExtractedFact


class FactExtractor:

    def __init__(self):

        self.llm = GroqClient()

    def extract(

        self,

        chunk

    ):

        result = self.llm.generate_json(

            prompt=chunk.content,

            system_prompt=FACT_EXTRACTION_PROMPT

        )

        facts = []

        for item in result:

            facts.append(

                ExtractedFact(

                    key=item["key"],

                    value=item["value"],

                    confidence=item.get(

                        "confidence",

                        1.0

                    )

                )

            )

        return facts