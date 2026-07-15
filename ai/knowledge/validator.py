class KnowledgeValidator:

    def validate(self, knowledge):

        knowledge.nodes = [

            node

            for node in knowledge.nodes

            if node.id

        ]

        knowledge.edges = [

            edge

            for edge in knowledge.edges

            if edge.source and edge.target

        ]

        return knowledge