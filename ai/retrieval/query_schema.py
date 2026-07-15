from indexing.graph_indexer import GraphIndexer
from indexing.vector_indexer import VectorIndexer
from indexing.index_models import IndexResult


class IndexManager:

    def __init__(self):

        self.graph = GraphIndexer()

        self.vector = VectorIndexer()

    def index(
        self,
        knowledge,
        vector_record
    ):

        graph_ops = self.graph.build(
            knowledge
        )

        vector_ops = self.vector.build(
            vector_record
        )

        return {

            "graph": graph_ops,

            "vector": vector_ops
        }