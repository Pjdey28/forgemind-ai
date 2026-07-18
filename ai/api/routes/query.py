from fastapi import APIRouter
from pydantic import BaseModel
from services.query_service import QueryService

router = APIRouter()
service = QueryService()

class Query(BaseModel):
    question: str

@router.post("/query")
def query(request: Query):
    # Return the AIResponse object directly for a flat JSON structure
    return service.ask(request.question)