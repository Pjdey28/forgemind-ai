from storage.neo4j.client import Neo4jClient

class Neo4jRepository:
    _mock_nodes = {}
    _mock_edges = []

    def __init__(self):
        self.is_mock = False
        try:
            self.client = Neo4jClient()
            self.client.driver.verify_connectivity()
        except Exception as e:
            self.is_mock = True

    def merge_node(self, node, doc_id: str):
        if self.is_mock:
            Neo4jRepository._mock_nodes[node.id] = {
                "id": node.id,
                "label": node.label,
                "properties": node.properties,
                "doc_id": doc_id
            }
            return

        query = f"""
        MERGE (n:`{node.label}` {{id: $id}})
        SET n += $properties, n.doc_id = $doc_id
        """
        with self.client.session() as session:
            session.run(
                query,
                id=node.id,
                properties=node.properties,
                doc_id=doc_id
            )

    def merge_edge(self, edge, doc_id: str):
        if self.is_mock:
            Neo4jRepository._mock_edges.append({
                "source": edge.source,
                "relation": edge.relation,
                "target": edge.target,
                "properties": edge.properties,
                "doc_id": doc_id
            })
            return

        query = f"""
        MATCH (a {{id: $source}})
        MATCH (b {{id: $target}})
        MERGE (a)-[r:`{edge.relation}`]->(b)
        SET r += $properties, r.doc_id = $doc_id
        """
        with self.client.session() as session:
            session.run(
                query,
                source=edge.source,
                target=edge.target,
                properties=edge.properties,
                doc_id=doc_id
            )

    def expand(self, entities: list, doc_ids: list | None = None):
        if self.is_mock:
            graph_context = []
            for edge in Neo4jRepository._mock_edges:
                if doc_ids and edge["doc_id"] not in doc_ids:
                    continue
                if edge["source"] in entities or edge["target"] in entities:
                    graph_context.append(
                        f"{edge['source']} -[{edge['relation']}]-> {edge['target']}"
                    )
            return graph_context[:50]

        params = {"entities": entities}
        if doc_ids:
            query = """
            MATCH (n)-[r]-(m)
            WHERE n.id IN $entities AND r.doc_id IN $doc_ids
            RETURN n.id AS source, type(r) AS relation, m.id AS target
            LIMIT 50
            """
            params["doc_ids"] = doc_ids
        else:
            # If no doc_ids are specified, expand across all documents.
            query = """
            MATCH (n)-[r]-(m)
            WHERE n.id IN $entities
            RETURN n.id AS source, type(r) AS relation, m.id AS target
            LIMIT 50
            """

        graph_context = []
        with self.client.session() as session:
            result = session.run(query, **params)
            for record in result:
                graph_context.append(
                    f"{record['source']} -[{record['relation']}]-> {record['target']}"
                )
        return graph_context

    def get_all_nodes_and_edges(self):
        if self.is_mock:
            return {
                "nodes": list(Neo4jRepository._mock_nodes.values()),
                "edges": Neo4jRepository._mock_edges
            }

        query_nodes = "MATCH (n) RETURN n.id AS id, labels(n)[0] AS label, n AS properties, n.doc_id AS doc_id"
        query_edges = "MATCH (a)-[r]->(b) RETURN a.id AS source, type(r) AS relation, b.id AS target, r AS properties, r.doc_id AS doc_id"
        nodes = []
        edges = []
        with self.client.session() as session:
            res_nodes = session.run(query_nodes)
            for record in res_nodes:
                nodes.append({
                    "id": record["id"],
                    "label": record["label"],
                    "properties": dict(record["properties"]) if record["properties"] else {},
                    "doc_id": record["doc_id"]
                })
            res_edges = session.run(query_edges)
            for record in res_edges:
                edges.append({
                    "source": record["source"],
                    "relation": record["relation"],
                    "target": record["target"],
                    "properties": dict(record["properties"]) if record["properties"] else {},
                    "doc_id": record["doc_id"]
                })
        return {"nodes": nodes, "edges": edges}

    def delete_by_doc_id(self, doc_id: str):
        if self.is_mock:
            Neo4jRepository._mock_nodes = {nid: n for nid, n in Neo4jRepository._mock_nodes.items() if n["doc_id"] != doc_id}
            Neo4jRepository._mock_edges = [e for e in Neo4jRepository._mock_edges if e["doc_id"] != doc_id]
            return

        query_nodes = "MATCH (n) WHERE n.doc_id = $doc_id DETACH DELETE n"
        query_edges = "MATCH ()-[r]->() WHERE r.doc_id = $doc_id DELETE r"
        with self.client.session() as session:
            session.run(query_nodes, doc_id=doc_id)
            session.run(query_edges, doc_id=doc_id)