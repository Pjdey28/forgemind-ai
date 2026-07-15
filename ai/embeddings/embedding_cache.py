import hashlib


class EmbeddingCache:

    @staticmethod
    def hash(text):

        return hashlib.sha256(

            text.encode()

        ).hexdigest()