class ContextCompressor:
    def compress(self, context, max_tokens=3000):
        # Prevent prompt token overflow by limiting total character count 
        # (Approx 4 chars per token)
        max_chars = max_tokens * 4
        current_chars = 0
        compressed_docs = []

        for doc in context.get("documents", []):
            doc_len = len(str(doc.get("content", "")))
            if current_chars + doc_len <= max_chars:
                compressed_docs.append(doc)
                current_chars += doc_len
            else:
                break # Drop remaining documents if we hit the limit

        context["documents"] = compressed_docs
        return context