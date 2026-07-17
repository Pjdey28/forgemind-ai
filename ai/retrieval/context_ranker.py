from sentence_transformers import CrossEncoder
from config.settings import settings

class ContextRanker:
    def __init__(self):
        # Initialize a cross-encoder model to re-rank the retrieved vector chunks
        # This gives production-grade accuracy beyond raw cosine similarity search
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rank(self, context, question):
        if not context or "documents" not in context or not context["documents"]:
            return context

        documents = context["documents"]
        
        # Build evaluation pairs: (Question, Chunk Content)
        pairs = [[question, doc.get("content", "")] for doc in documents]
        
        # Compute exact semantic relevance scores
        scores = self.model.predict(pairs)
        
        # Assign scores to documents and sort descending
        for idx, score in enumerate(scores):
            documents[idx]["rerank_score"] = float(score)
            
        documents.sort(key=lambda x: x["rerank_score"], reverse=True)
        
        # Keep only the top 4 highly relevant chunks to prevent LLM prompt token bloat
        context["documents"] = documents[:4]
        return context