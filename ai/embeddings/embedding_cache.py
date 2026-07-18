import hashlib

class EmbeddingCache:
    def __init__(self):
        self._cache = {}

    def get(self, text: str):
        text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        return self._cache.get(text_hash)

    def set(self, text: str, embedding: list[float]):
        text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        self._cache[text_hash] = embedding
        
    def clear(self):
        self._cache.clear()