from embeddings.embedding_document import EmbeddingDocument


class EmbeddingBuilder:

    def build(self, chunk, knowledge):

        metadata = {

            "document": chunk.metadata.get("filename"),

            "section": chunk.section

        }

        content = []

        content.append(f"Section : {chunk.section}")

        for node in knowledge.nodes:

            content.append(

                f"{node.label} : {node.id}"

            )

        content.append("")

        content.append(chunk.text)

        return EmbeddingDocument(

            id=chunk.chunk_id,

            content="\n".join(content),

            metadata=metadata

        )