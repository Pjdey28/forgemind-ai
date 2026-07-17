from knowledge.knowledge_models import (
    KnowledgeObject,
    KnowledgeNode,
    KnowledgeEdge,
    KnowledgeFact
)
from knowledge.normalizer import KnowledgeNormalizer

class KnowledgeBuilder:
    def build(self, extraction_result):
        knowledge = KnowledgeObject()

        # 1. Process Nodes with aggressive ID normalization
        for entity in extraction_result.entities:
            normalized_id = KnowledgeNormalizer.normalize_id(entity.id)
            knowledge.nodes.append(
                KnowledgeNode(
                    id=normalized_id, 
                    label=entity.label, 
                    properties=entity.properties
                )
            )

        # 2. Process Edges matching the normalized IDs
        for relation in extraction_result.relationships:
            normalized_source = KnowledgeNormalizer.normalize_id(relation.source)
            normalized_target = KnowledgeNormalizer.normalize_id(relation.target)
            normalized_relation = KnowledgeNormalizer.normalize_relation(relation.relation)

            knowledge.edges.append(
                KnowledgeEdge(
                    source=normalized_source, 
                    relation=normalized_relation, 
                    target=normalized_target, 
                    properties=relation.properties
                )
            )

        # 3. Process Facts
        for fact in extraction_result.facts:
            knowledge.facts.append(
                KnowledgeFact(
                    subject=KnowledgeNormalizer.normalize_id(fact.key), 
                    predicate="HAS_VALUE", 
                    value=str(fact.value)
                )
            )

        return knowledge