class GraphIndexer:

    def build(self, knowledge):

        commands = []

        for node in knowledge.nodes:

            commands.append({
                "operation": "MERGE_NODE",
                "node": node
            })

        for edge in knowledge.edges:

            commands.append({
                "operation": "MERGE_EDGE",
                "edge": edge
            })

        return commands