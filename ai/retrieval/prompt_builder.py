from llm.prompt_manager import PromptManager

class PromptBuilder:
    CORE_RULES = """
    Answer ONLY from the supplied context. Never hallucinate. 
    If the answer is unavailable, state: "INSUFFICIENT DATA."
    Always cite supporting documents and graph relationships.
    """

    def build(self, question, context, agent_type="GENERAL_OPERATIONS_AGENT"):
        documents = [str(doc.get("content", "")) for doc in context.get("documents", [])]
        graph_lines = [str(edge) for edge in context.get("graph", [])]
        personas = {
            "MAINTENANCE_AGENT": PromptManager.MAINTENANCE_AGENT,
            "COMPLIANCE_AGENT": PromptManager.COMPLIANCE_AGENT,
            "GENERAL_OPERATIONS_AGENT": PromptManager.GENERAL_OPERATIONS_AGENT,
            "QA_SYSTEM": PromptManager.QA_SYSTEM,
            "RCA_SYSTEM": PromptManager.RCA_SYSTEM
        }
        
        active_persona = personas.get(agent_type, PromptManager.GENERAL_OPERATIONS_AGENT)

        return f"""
System Persona: {active_persona}
{self.CORE_RULES}

Knowledge Graph Architecture:
{chr(10).join(graph_lines)}

Document Segments Context:
{chr(10).join(documents)}

Operator Question: {question}
Answer:
"""