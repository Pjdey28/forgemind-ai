class PromptBuilder:
    SYSTEM_PROMPT = """
You are an Industrial RAG Operator Copilot Brain.
Answer ONLY from the supplied context.
Never hallucinate.
If the answer is unavailable, clearly say so.
Always cite the supporting documents.
"""

    def build(self, question, context):
        documents = [str(doc.get("content", "")) for doc in context.get("documents", [])]
        graph_lines = [str(edge) for edge in context.get("graph", [])]

        return f"""
Knowledge Graph Architecture:
{chr(10).join(graph_lines)}

Document Segments Context:
{chr(10).join(documents)}

Operator Question: {question}
Answer:
"""