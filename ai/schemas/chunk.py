from pydantic import BaseModel, Field
from typing import Any


class KnowledgeChunk(BaseModel):

    chunk_id: str

    text: str

    section: str

    metadata: dict[str, Any] = Field(default_factory=dict)

    entities: dict[str, Any] = Field(default_factory=dict)

    relationships: list[dict[str, Any]] = Field(default_factory=list)

    facts: list[dict[str, Any]] = Field(default_factory=list)