from retrieval.query_understanding import QueryUnderstanding
from retrieval.semantic_retriever import SemanticRetriever
from retrieval.graph_retriever import GraphRetriever
from retrieval.context_fusion import ContextFusion
from retrieval.context_ranker import ContextRanker
from retrieval.prompt_builder import PromptBuilder
from embeddings.embedding_model import EmbeddingModel
from storage.chroma.repository import ChromaRepository
from storage.neo4j.repository import Neo4jRepository

class IntentContainer:
    def __init__(self, data: dict):
        self.intent = data.get("Intent", "")
        self.entities = data.get("Entities", [])
        self.time = data.get("Time", "")
        self.filters = data.get("Filters", {})

class RetrievalEngine:
    def __init__(self):
        self.query = QueryUnderstanding()
        self.embedding = EmbeddingModel()
        
        # Inject required persistence architecture parameters
        self.chroma_repo = ChromaRepository()
        self.neo4j_repo = Neo4jRepository()
        
        self.semantic = SemanticRetriever(repository=self.chroma_repo)
        self.graph = GraphRetriever(repository=self.neo4j_repo)
        
        self.fusion = ContextFusion()
        self.ranker = ContextRanker()
        self.prompt = PromptBuilder()

    def retrieve(self, question: str) -> tuple:
        raw_intent = self.query.understand(question)
        intent_obj = IntentContainer(raw_intent)

        query_vector = self.embedding.embed(question)

        documents = self.semantic.retrieve(
            embedding=query_vector,
            filters=intent_obj.filters
        )

        graph_nodes = self.graph.retrieve(
            entities=intent_obj.entities
        )

        context = self.fusion.merge(documents, graph_nodes)
        context = self.ranker.rank(context)

        return self.prompt.build(question, context), context