import uuid

from chunking.base_chunker import BaseChunker
from chunking.chunk_models import Chunk
from chunking.section_detector import SectionDetector


class IndustrialChunker(BaseChunker):

    def __init__(self):

        self.detector = SectionDetector()

    def chunk(self, document):

        lines = document.text.split("\n")

        chunks = []

        current_section = "General"

        current_text = []

        for line in lines:

            if self.detector.is_heading(line):

                if current_text:

                    chunks.append(

                        Chunk(

                            chunk_id=str(uuid.uuid4()),

                            text="\n".join(current_text),

                            section=current_section,

                            metadata=document.metadata

                        )

                    )

                    current_text = []

                current_section = line.strip()

            current_text.append(line)

        if current_text:

            chunks.append(

                Chunk(

                    chunk_id=str(uuid.uuid4()),

                    text="\n".join(current_text),

                    section=current_section,

                    metadata=document.metadata

                )

            )

        return chunks