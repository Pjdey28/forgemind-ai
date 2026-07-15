from storage.chroma.collection import CollectionManager


class ChromaRepository:

    def __init__(self):

        self.collection = CollectionManager().get_collection()

    def add(self, record):

        self.collection.add(

            ids=[record.id],

            embeddings=[record.embedding],

            documents=[record.content],

            metadatas=[record.metadata]

        )