from storage.chroma.client import ChromaClient


class CollectionManager:

    def __init__(self):

        client = ChromaClient().get_client()

        self.collection = client.get_or_create_collection(
            name="industrial_documents"
        )

    def get_collection(self):

        return self.collection