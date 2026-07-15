class EvidenceValidator:

    def validate(self, context):

        documents = {}

        for chunk in context["documents"]:

            key = (
                chunk.metadata.get("filename"),
                chunk.chunk_id
            )

            documents[key] = chunk

        context["documents"] = list(documents.values())

        return context