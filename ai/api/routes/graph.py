from fastapi import APIRouter
from storage.neo4j.repository import Neo4jRepository

router = APIRouter(prefix="/graph", tags=["graph"])

@router.get("/all")
def get_all_graph():
    repo = Neo4jRepository()
    return repo.get_all_nodes_and_edges()

@router.get("/stats")
def get_graph_stats():
    repo = Neo4jRepository()
    data = repo.get_all_nodes_and_edges()
    return {
        "nodes_count": len(data["nodes"]),
        "edges_count": len(data["edges"])
    }
