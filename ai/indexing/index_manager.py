from storage.neo4j.repository import Neo4jRepository
from storage.chroma.repository import ChromaRepository

class IndexManager:
    def __init__(self):
        self.graph_repo = Neo4jRepository()
        self.vector_repo = ChromaRepository()

    def execute(self, knowledge, vector_record):
        for node in knowledge.nodes:
            self.graph_repo.merge_node(node)
        for edge in knowledge.edges:
            self.graph_repo.merge_edge(edge)
        self.vector_repo.add(vector_record)