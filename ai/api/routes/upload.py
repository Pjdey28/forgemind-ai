import os
from fastapi import APIRouter, UploadFile
from services.ingestion_service import IngestionService

router = APIRouter()
service = IngestionService()

@router.post("/upload")
async def upload(file: UploadFile):
    # Ensure the upload directory exists to prevent FileNotFoundError
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    path = f"{upload_dir}/{file.filename}"
    
    with open(path, "wb") as f:
        f.write(await file.read())
        
    res = service.ingest(path)
    
    return {
        "status": "success",
        "doc_id": res["doc_id"],
        "filename": res["filename"],
        "chunks_count": res["chunks_count"]
    }

@router.delete("/upload/{doc_id}")
def delete_document(doc_id: str):
    # 1. Clear vector database index
    from storage.chroma.repository import ChromaRepository
    chroma = ChromaRepository()
    chroma.delete(doc_id)
    
    # 2. Clear Knowledge Graph nodes/edges
    from storage.neo4j.repository import Neo4jRepository
    graph = Neo4jRepository()
    graph.delete_by_doc_id(doc_id)
    
    return {
        "status": "success",
        "message": f"Document index with doc_id {doc_id} successfully deleted."
    }