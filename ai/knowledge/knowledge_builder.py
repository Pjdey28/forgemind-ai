from knowledge.knowledge_models import KnowledgeObject, KnowledgeNode, KnowledgeEdge, KnowledgeFact

class KnowledgeBuilder:
    def build(self, extraction_result):
        knowledge = KnowledgeObject()

        # Iterate directly across the structured extraction arrays
        for entity in extraction_result.entities:
            knowledge.nodes.append(
                KnowledgeNode(id=entity.id, label=entity.label, properties=entity.properties)
            )

        for relation in extraction_result.relationships:
            knowledge.edges.append(
                KnowledgeEdge(source=relation.source, relation=relation.relation, target=relation.target, properties=relation.properties)
            )

        for fact in extraction_result.facts:
            knowledge.facts.append(
                KnowledgeFact(subject=fact.key, predicate="has_value", value=str(fact.value))
            )

        return knowledge