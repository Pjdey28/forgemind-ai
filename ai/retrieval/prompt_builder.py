class PromptBuilder:

    SYSTEM_PROMPT = """
You are IndustrialBrain AI.

Answer ONLY from the supplied context.

Never hallucinate.

If the answer is unavailable, clearly say so.

Always cite the supporting documents.
"""

    def build(

        self,

        question,

        context

    ):

        documents = []

        for doc in context["documents"]:

            documents.append(doc.content)

        graph = []

        for node in context["graph"]:

            graph.append(str(node))

        return f"""

Question

{question}

Knowledge Graph

{chr(10).join(graph)}

Documents

{chr(10).join(documents)}

"""