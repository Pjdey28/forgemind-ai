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
        
    service.ingest(path)
    
    return {
        "status": "success"
    }