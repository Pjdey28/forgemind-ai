from retrieval.retrieval_engine import RetrievalEngine
from reasoning.reasoning_engine import ReasoningEngine
from reasoning.citation_generator import CitationGenerator
from reasoning.response_builder import ResponseBuilder


class QueryService:

    def __init__(self):

        self.retriever = RetrievalEngine()

        self.reasoner = ReasoningEngine()

        self.citations = CitationGenerator()

        self.builder = ResponseBuilder()

    def ask(self, question):

        prompt, context = self.retriever.retrieve(question)

        answer = self.reasoner.answer(prompt)

        citations = self.citations.build(context)

        return self.builder.build(
            answer=answer,
            confidence=0.95,
            citations=citations
        )