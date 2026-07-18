from pathlib import Path
from datetime import datetime
from parsers.parser_factory import ParserFactory
from schemas.document import DocumentSchema
from utils.metadata import build_metadata
from chunking.industrial_chunker import IndustrialChunker

class DocumentLoader:
    def __init__(self):
        self.chunker = IndustrialChunker()

    def load(self, file_path: str) -> dict:
        extension = Path(file_path).suffix.lower()
        parser = ParserFactory.get_parser(extension)
        text = parser.parse(file_path)
        metadata = build_metadata(file_path)

        document = DocumentSchema(
            filename=metadata["filename"],
            filetype=extension,
            text=text,
            metadata=metadata,
            processed_at=datetime.utcnow()
        )
        document.metadata["doc_id"] = document.doc_id
        
        chunks = self.chunker.chunk(document)
        return {
            "document": document,
            "chunks": chunks
        }