from retrieval.query_understanding import QueryUnderstanding
from retrieval.semantic_retriever import SemanticRetriever
from retrieval.graph_retriever import GraphRetriever
from retrieval.context_fusion import ContextFusion
from retrieval.context_ranker import ContextRanker
from retrieval.prompt_builder import PromptBuilder
from embeddings.embedding_model import EmbeddingModel
from storage.chroma.repository import ChromaRepository
from storage.neo4j.repository import Neo4jRepository
from reasoning.evidence_validator import EvidenceValidator
from reasoning.context_compressor import ContextCompressor

class IntentContainer:
    def __init__(self, data: dict):
        if not isinstance(data, dict):
            data = {} 
        self.intent = data.get("Intent", "")
        self.agent_type = data.get("AgentType", "GENERAL_OPERATIONS_AGENT") 
        self.entities = data.get("Entities", [])
        self.time = data.get("Time", "")
        self.filters = data.get("Filters", {})

class RetrievalEngine:
    def __init__(self):
        self.query = QueryUnderstanding()
        self.embedding = EmbeddingModel()
        self.chroma_repo = ChromaRepository()
        self.neo4j_repo = Neo4jRepository()
        self.semantic = SemanticRetriever(repository=self.chroma_repo)
        self.graph = GraphRetriever(repository=self.neo4j_repo)
        self.fusion = ContextFusion()
        self.ranker = ContextRanker()
        self.validator = EvidenceValidator()
        self.compressor = ContextCompressor()
        self.prompt = PromptBuilder()

    def retrieve(self, question: str) -> tuple:
        # 1. Classify Intent and route agent
        raw_intent = self.query.understand(question)
        intent_obj = IntentContainer(raw_intent)

        # 2. Convert query to vector
        query_vector = self.embedding.embed(question)

        # 3. Retrieve chunks and graph context
        documents = self.semantic.retrieve(
            embedding=query_vector,
            filters=intent_obj.filters
        )
        graph_nodes = self.graph.retrieve(
            entities=intent_obj.entities
        )

        # 4. Process Context (Fuse -> Rank -> Validate -> Compress)
        context = self.fusion.merge(documents, graph_nodes)
        context = self.ranker.rank(context, question)
        context = self.validator.validate(context)
        context = self.compressor.compress(context)

        # 5. Build Final Prompt with specialized Agent Persona
        final_prompt = self.prompt.build(question, context, intent_obj.agent_type)
        
        return final_prompt, context