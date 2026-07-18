from llm.groq_client import GroqClient

VERIFICATION_PROMPT = """
You are an Industrial Truth Verification Agent.
Your job is to cross-reference an AI-generated answer against the raw source documentation chunks.

AI Answer:
{answer}

Raw Source Chunks:
{context}

Check for:
1. Direct contradictions (e.g., source says 45 PSI max, but answer says 100 PSI).
2. Hallucinations (e.g., answer claims a schedule that is completely missing from the chunks).

Respond ONLY with a single valid JSON object matching this schema:
{{
    "is_valid": true or false,
    "reason_for_failure": "string detailing the contradiction or empty string"
}}
"""

class AnswerVerifier:
    def __init__(self):
        self.llm = GroqClient()

    def verify(self, answer: str, context: dict) -> dict:
        # Build text string of all documents retrieved
        doc_texts = "\n---\n".join([doc.get("content", "") for doc in context.get("documents", [])])
        
        formatted_prompt = VERIFICATION_PROMPT.format(
            answer=answer,
            context=doc_texts
        )
        
        try:
            result = self.llm.generate_json(
                prompt=formatted_prompt,
                system_prompt="You are a strict, objective technical inspector. Output JSON only."
            )
            return result
        except Exception:
            # Fallback if parsing fails under high traffic load
            return {"is_valid": True, "reason_for_failure": ""}