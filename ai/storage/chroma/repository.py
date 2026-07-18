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

    def search(self, embedding, filters=None, top_k=5):
        # Added search method for SemanticRetriever
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            where=filters if filters else None
        )
        
        documents = []
        if results and "documents" in results and results["documents"]:
            # Format results to pass back to the context fusion engine
            for idx, doc_text in enumerate(results["documents"][0]):
                documents.append({
                    "id": results["ids"][0][idx],
                    "content": doc_text,
                    "metadata": results["metadatas"][0][idx] if results["metadatas"] else {}
                })
                
        return documents

    def delete(self, doc_id: str):
        self.collection.delete(where={"doc_id": doc_id})