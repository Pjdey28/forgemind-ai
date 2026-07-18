from retrieval.retrieval_engine import RetrievalEngine
from reasoning.reasoning_engine import ReasoningEngine
from reasoning.citation_generator import CitationGenerator
from reasoning.response_builder import ResponseBuilder
from reasoning.verifier import AnswerVerifier

class QueryService:
    def __init__(self):
        self.retriever = RetrievalEngine()
        self.reasoner = ReasoningEngine()
        self.citations = CitationGenerator()
        self.verifier = AnswerVerifier()  # Now connected
        self.builder = ResponseBuilder()

    def ask(self, question: str):
        # 1. Retrieve raw vector chunks and graph edges
        prompt, context = self.retriever.retrieve(question)

        # 2. Re-rank documents based on the question (We handle this inside retrieval engine now)
        # 3. Generate primary response from Groq
        answer = self.reasoner.answer(prompt)

        # 4. Verification Check Loop
        verification = self.verifier.verify(answer, context)
        
        if not verification.get("is_valid", True):
            # Self-Correction: Re-prompt Groq with the exact error found by the verifier
            correction_prompt = f"""
            {prompt}
            
            CRITICAL CORRECTION REQUIRED: Your previous answer contained an inaccuracy or contradiction:
            "{verification.get('reason_for_failure')}"
            
            Please re-evaluate the source data and provide a corrected answer.
            """
            answer = self.reasoner.answer(correction_prompt)

        # 5. Extract citations and map clean JSON output structures
        citations = self.citations.build(context)

        return self.builder.build(
            answer=answer,
            confidence=0.98 if verification.get("is_valid") else 0.85,
            citations=citations
        )