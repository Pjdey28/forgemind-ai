# ai/embeddings/embedding_service.py
from embeddings.embedding_builder import EmbeddingBuilder
from embeddings.embedding_model import EmbeddingModel
from embeddings.vector_record import VectorRecord
from embeddings.embedding_cache import EmbeddingCache

class EmbeddingService:
    def __init__(self):
        self.builder = EmbeddingBuilder()
        self.model = EmbeddingModel()
        self.cache = EmbeddingCache()

    def create_vector_record(self, chunk, knowledge):
        # 1. Build the document string
        document = self.builder.build(chunk, knowledge)

        # 2. Check the cache 
        cached_vector = self.cache.get(document.content)
        
        if cached_vector:
            vector = cached_vector
        else:
            # 3. Compute the vector only if it's a new, unseen text chunk
            vector = self.model.embed(document.content)
            self.cache.set(document.content, vector)  # Save it

        return VectorRecord(
            id=document.id,
            embedding=vector,
            content=document.content,
            metadata=document.metadata,
            source_document=document.metadata.get("filename", ""),
            graph_node_ids=[node.id for node in knowledge.nodes],
            graph_edge_count=len(knowledge.edges)
        )