from parsers.base_parser import BaseParser
from llm.groq_client import GroqClient

class ImageParser(BaseParser):
    def __init__(self):
        self.llm = GroqClient()
        self.vision_prompt = """
        Analyze this industrial diagram, P&ID (Piping and Instrumentation Diagram), or schematic in extreme technical detail.
        1. List all equipment tags, valves, pumps, and sensors by their ID.
        2. Describe the physical topology: which equipment connects to which, and what is the flow direction?
        3. Extract any tables, setpoints, or parameter thresholds visible in the image.
        Output a highly structured, comprehensive technical report of everything visible.
        """

    def parse(self, file_path: str) -> str:
        # Transforms a flat image into rich semantic text for the chunker
        return self.llm.generate_vision(file_path, self.vision_prompt)