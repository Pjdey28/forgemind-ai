from storage.neo4j.repository import Neo4jRepository
from indexing.graph_indexer import GraphIndexer
from indexing.vector_indexer import VectorIndexer
from indexing.index_models import IndexResult
from storage.chroma.repository import ChromaRepository


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
    def execute(

        self,

        knowledge,

        vector_record

    ):

        graph_repo = Neo4jRepository()

        vector_repo = ChromaRepository()

        for node in knowledge.nodes:

            graph_repo.merge_node(node)

        for edge in knowledge.edges:

            graph_repo.merge_edge(edge)

        vector_repo.add(vector_record)