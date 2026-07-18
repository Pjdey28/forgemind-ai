class VectorIndexer:

    def build(
        self,
        vector_record
    ):

        return {

            "id": vector_record.id,

            "embedding": vector_record.embedding,

            "content": vector_record.content,

            "metadata": vector_record.metadata

        }