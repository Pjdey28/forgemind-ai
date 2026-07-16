class EvidenceValidator:
    def validate(self, context):
        documents = {}
        for chunk in context["documents"]:
            metadata = chunk.get("metadata", {})
            # Fixed: Dictionary access
            key = (metadata.get("filename"), chunk.get("id"))
            documents[key] = chunk
            
        context["documents"] = list(documents.values())
        return context