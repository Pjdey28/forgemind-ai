from pathlib import Path
from datetime import datetime
from unittest import loader


from parsers.parser_factory import ParserFactory
from schemas.document import DocumentSchema
from utils.metadata import build_metadata
from chunking.industrial_chunker import IndustrialChunker

class DocumentLoader:

    def load(self, file_path: str):

        extension = Path(file_path).suffix.lower()

        parser = ParserFactory.get_parser(extension)

        text = parser.parse(file_path)

        metadata = build_metadata(file_path)
        loader = IndustrialChunker()

        document = DocumentSchema(
            filename=metadata["filename"],
            filetype=extension,
            text=text,
            metadata=metadata
        )
        chunks = loader.chunk(document)
        return {
            "document": document,
            "chunks": chunks
        }

