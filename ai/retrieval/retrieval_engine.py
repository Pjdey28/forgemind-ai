from retrieval.query_understanding import QueryUnderstanding
from retrieval.semantic_retriever import SemanticRetriever
from retrieval.graph_retriever import GraphRetriever
from retrieval.context_fusion import ContextFusion
from retrieval.context_ranker import ContextRanker
from retrieval.prompt_builder import PromptBuilder

from embeddings.embedding_model import EmbeddingModel


class RetrievalEngine:

    def __init__(self):

        self.query = QueryUnderstanding()

        self.embedding = EmbeddingModel()

        self.semantic = SemanticRetriever()

        self.graph = GraphRetriever()

        self.fusion = ContextFusion()

        self.ranker = ContextRanker()

        self.prompt = PromptBuilder()

    def retrieve(self, question):

        intent = self.query.understand(question)

        query_vector = self.embedding.embed(question)

        documents = self.semantic.retrieve(
            embedding=query_vector,
            filters=intent.filters
        )

        graph = self.graph.retrieve(
            entities=intent.entities
        )

        context = self.fusion.merge(
            documents,
            graph
        )

        context = self.ranker.rank(
            context
        )

        return (self.prompt.build(
            question,
            context
        ),context)