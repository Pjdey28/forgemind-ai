from pydantic import BaseModel, Field
from typing import Any


class ExtractedEntity(BaseModel):
    id: str
    label: str
    properties: dict[str, Any] = Field(default_factory=dict)


class ExtractedRelationship(BaseModel):
    source: str
    target: str
    relation: str
    properties: dict[str, Any] = Field(default_factory=dict)


class ExtractedFact(BaseModel):
    key: str
    value: Any
    confidence: float = 1.0


class ExtractionResult(BaseModel):

    entities: list[ExtractedEntity] = Field(default_factory=list)

    relationships: list[ExtractedRelationship] = Field(default_factory=list)

    facts: list[ExtractedFact] = Field(default_factory=list)