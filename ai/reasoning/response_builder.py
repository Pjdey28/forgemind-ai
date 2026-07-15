from pydantic import BaseModel
from typing import Any


class AIResponse(BaseModel):

    answer: str

    confidence: float

    citations: list[dict[str, Any]]

    metadata: dict[str, Any]


class ResponseBuilder:

    def build(
        self,
        answer,
        confidence,
        citations
    ):

        return AIResponse(

            answer=answer,

            confidence=confidence,

            citations=citations,

            metadata={}
        )