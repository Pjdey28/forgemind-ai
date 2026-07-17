class EvidenceValidator:
    def validate(self, context):
        # Filter out chunks that have empty content or corrupted metadata
        valid_docs = []
        for chunk in context.get("documents", []):
            if chunk.get("content") and isinstance(chunk.get("metadata"), dict):
                valid_docs.append(chunk)
        
        context["documents"] = valid_docs
        return context