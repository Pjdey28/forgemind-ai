class CitationGenerator:
    def build(self, context):
        citations = []
        if "documents" in context:
            for doc in context["documents"]:
                meta = doc.get("metadata", {})
                citations.append({
                    "document": meta.get("filename", "unknown_source.pdf"),
                    "chunk": doc.get("id", "unknown_id")
                })
        return citations