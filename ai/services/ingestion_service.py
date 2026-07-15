from ingestion.document_loader import DocumentLoader

from processing.cleaner import TextCleaner
from processing.metadata import MetadataExtractor
from processing.normalizer import TextNormalizer

from chunking.industrial_chunker import IndustrialChunker

from extraction.extractor import IndustrialExtractor

from knowledge.knowledge_builder import KnowledgeBuilder

from embeddings.embedding_service import EmbeddingService

from services.indexing_service import IndexingService


class IngestionService:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = IndustrialChunker()

        self.extractor = IndustrialExtractor()

        self.builder = KnowledgeBuilder()

        self.embedding = EmbeddingService()

        self.indexing = IndexingService()

    def ingest(
        self,
        path: str
    ):

        # Step 1
        document = self.loader.load(path)

        # Step 2
        document.content = TextCleaner.clean(
            document.content
        )

        document.content = TextNormalizer.normalize(
            document.content
        )

        document.metadata.update(

            MetadataExtractor.extract(
                document
            )

        )

        # Step 3
        chunks = self.chunker.chunk(
            document
        )

        # Step 4
        for chunk in chunks:

            extraction = self.extractor.extract(
                chunk
            )

            # Step 5
            knowledge = self.builder.build(
                extraction
            )

            # Step 6
            vector_record = self.embedding.create_vector_record(

                chunk,

                knowledge

            )

            # Step 7
            self.indexing.index(

                knowledge,

                vector_record

            )

        return True