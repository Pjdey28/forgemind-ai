from pydantic import BaseModel, Field
from typing import Any


class VectorRecord(BaseModel):

    id: str

    embedding: list[float]

    content: str

    metadata: dict[str, Any] = Field(default_factory=dict)

    graph_node_ids: list[str] = Field(default_factory=list)

    graph_edge_count: int = 0

    source_document: str = ""