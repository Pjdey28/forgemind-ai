from storage.neo4j.client import Neo4jClient

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

    def expand(self, entities, depth=2):
        # Added expand method for GraphRetriever
        if not entities:
            return []
            
        # Basic implementation to fetch immediate relationships
        query = """
        MATCH (n)-[r]-(m)
        WHERE n.id IN $entities
        RETURN n.id AS source, type(r) AS relation, m.id AS target
        LIMIT 50
        """
        graph_context = []
        with self.client.session() as session:
            result = session.run(query, entities=entities)
            for record in result:
                graph_context.append(
                    f"{record['source']} -[{record['relation']}]-> {record['target']}"
                )
                
        return graph_context