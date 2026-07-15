class KnowledgeDeduplicator:

    def deduplicate(self, knowledge):

        unique = {}

        for node in knowledge.nodes:

            unique[node.id] = node

        knowledge.nodes = list(unique.values())

        return knowledge