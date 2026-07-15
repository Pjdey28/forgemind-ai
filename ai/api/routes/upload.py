from fastapi import APIRouter

from fastapi import UploadFile

from services.ingestion_service import IngestionService


router = APIRouter()

service = IngestionService()


@router.post("/upload")

async def upload(

    file: UploadFile

):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as f:

        f.write(await file.read())

    service.ingest(path)

    return {

        "status": "success"

    }