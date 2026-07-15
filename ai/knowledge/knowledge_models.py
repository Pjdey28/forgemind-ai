from pydantic import BaseModel, Field
from typing import Any


class KnowledgeNode(BaseModel):

    id: str

    label: str

    properties: dict[str, Any] = Field(default_factory=dict)


class KnowledgeEdge(BaseModel):

    source: str

    relation: str

    target: str

    properties: dict[str, Any] = Field(default_factory=dict)


class KnowledgeFact(BaseModel):

    subject: str

    predicate: str

    value: str


class KnowledgeObject(BaseModel):

    nodes: list[KnowledgeNode] = Field(default_factory=list)

    edges: list[KnowledgeEdge] = Field(default_factory=list)

    facts: list[KnowledgeFact] = Field(default_factory=list)