class SemanticRetriever:

    def __init__(self, repository):
        self.repository = repository

    def retrieve(self, embedding, filters=None, top_k=5):
        # Pass the extracted metadata filters directly into the ChromaDB query layer
        # ChromaDB expects a dict format like {"zone": "Sector B"} or {"extension": ".pdf"}
        chroma_filters = {}
        if filters and isinstance(filters, dict):
            # Clean up empty filter keys if any exist
            chroma_filters = {k: v for k, v in filters.items() if v}

        return self.repository.search(
            embedding=embedding,
            filters=chroma_filters if chroma_filters else None,
            top_k=top_k
        )