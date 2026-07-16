from knowledge.knowledge_models import (
    KnowledgeObject,
    KnowledgeNode,
    KnowledgeEdge,
    KnowledgeFact
)

class KnowledgeBuilder:
    def build(self, extraction_result):
        knowledge = KnowledgeObject()

        # 1. Process Nodes with aggressive ID normalization
        for entity in extraction_result.entities:
            # Force the ID to be uppercase to prevent duplicates in Neo4j
            normalized_id = str(entity.id).strip().upper()
            
            knowledge.nodes.append(
                KnowledgeNode(
                    id=normalized_id, 
                    label=entity.label, 
                    properties=entity.properties
                )
            )

        # 2. Process Edges matching the normalized IDs
        for relation in extraction_result.relationships:
            normalized_source = str(relation.source).strip().upper()
            normalized_target = str(relation.target).strip().upper()
            normalized_relation = str(relation.relation).strip().upper().replace(" ", "_")
            
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
                    subject=str(fact.key).strip().upper(), 
                    predicate="HAS_VALUE", 
                    value=str(fact.value)
                )
            )

        return knowledge