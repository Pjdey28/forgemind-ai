from pydantic import BaseModel, Field
from typing import Any


class EmbeddingDocument(BaseModel):

    id: str

    content: str

    metadata: dict[str, Any] = Field(default_factory=dict)