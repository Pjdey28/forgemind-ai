from neo4j.client import Neo4jClient


class Neo4jRepository:

    def __init__(self):

        self.client = Neo4jClient()

    def merge_node(self, node):

        query = f"""

        MERGE (n:{node.label} {{id:$id}})

        SET n += $properties

        """

        with self.client.session() as session:

            session.run(

                query,

                id=node.id,

                properties=node.properties

            )

    def merge_edge(self, edge):

        query = """

        MATCH (a {id:$source})

        MATCH (b {id:$target})

        MERGE (a)-[r:RELATED {type:$relation}]->(b)

        """

        with self.client.session() as session:

            session.run(

                query,

                source=edge.source,

                target=edge.target,

                relation=edge.relation

            )