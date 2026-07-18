import chromadb

from config.settings import settings


class ChromaClient:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB
        )

    def get_client(self):
        return self.client