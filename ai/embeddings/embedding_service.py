from embeddings.embedding_builder import EmbeddingBuilder
from embeddings.embedding_model import EmbeddingModel
from embeddings.vector_record import VectorRecord


class EmbeddingService:

    def __init__(self):

        self.builder = EmbeddingBuilder()

        self.model = EmbeddingModel()

    def create_vector_record(

        self,

        chunk,

        knowledge

    ):

        document = self.builder.build(

            chunk,

            knowledge

        )

        vector = self.model.embed(

            document.content

        )

        return VectorRecord(

            id=document.id,

            embedding=vector,

            content=document.content,

            metadata=document.metadata,

            source_document=document.metadata.get(

                "filename",

                ""

            ),

            graph_node_ids=[

                node.id

                for node in knowledge.nodes

            ],

            graph_edge_count=len(

                knowledge.edges

            )

        )