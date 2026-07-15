from pydantic import BaseModel, Field
from typing import Any


class IndexResult(BaseModel):

    chunk_id: str

    vector_indexed: bool = False

    graph_indexed: bool = False

    vector_id: str | None = None

    node_count: int = 0

    edge_count: int = 0

    metadata: dict[str, Any] = Field(default_factory=dict)