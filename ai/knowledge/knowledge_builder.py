from knowledge.knowledge_models import (
    KnowledgeObject,
    KnowledgeNode,
    KnowledgeEdge,
    KnowledgeFact
)


class KnowledgeBuilder:

    def build(self, chunk):

        knowledge = KnowledgeObject()

        entities = chunk.entities

        for entity_type, values in entities.items():

            if isinstance(values, list):

                for value in values:

                    if isinstance(value, dict):

                        node = KnowledgeNode(

                            id=value.get(
                                "id",
                                value.get(
                                    "name",
                                    str(value)
                                )
                            ),

                            label=entity_type,

                            properties=value

                        )

                    else:

                        node = KnowledgeNode(

                            id=str(value),

                            label=entity_type

                        )

                    knowledge.nodes.append(node)

        for relation in chunk.relationships:

            knowledge.edges.append(

                KnowledgeEdge(

                    source=relation["source"],

                    relation=relation["relation"],

                    target=relation["target"]

                )

            )

        for fact in chunk.facts:

            knowledge.facts.append(

                KnowledgeFact(**fact)

            )

        return knowledge