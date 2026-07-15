from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(

            "BAAI/bge-large-en-v1.5"

        )

    def embed(

        self,

        text: str

    ) -> list[float]:

        embedding = self.model.encode(

            text,

            normalize_embeddings=True

        )

        return embedding.tolist()