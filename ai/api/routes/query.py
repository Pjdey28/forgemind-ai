from fastapi import APIRouter

from pydantic import BaseModel

from services.query_service import QueryService


router = APIRouter()

service = QueryService()


class Query(BaseModel):

    question: str


@router.post("/query")

def query(

    request: Query

):

    answer = service.ask(

        request.question

    )

    return {

        "answer": answer

    }