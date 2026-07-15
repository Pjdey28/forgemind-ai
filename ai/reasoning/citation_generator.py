class CitationGenerator:

    def build(

        self,

        context

    ):

        citations = []

        for doc in context["documents"]:

            citations.append({

                "document": doc.metadata.get("filename"),

                "chunk": doc.chunk_id

            })

        return citations