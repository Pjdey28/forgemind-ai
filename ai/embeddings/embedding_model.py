from sentence_transformers import SentenceTransformer
from config.settings import settings

class EmbeddingModel:
    def __init__(self):
        # Dynamically load the model from environment settings
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed(self, text: str) -> list[float]:
        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )
        return embedding.tolist()