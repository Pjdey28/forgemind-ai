from pydantic import BaseModel, Field
from typing import Dict, Any, List

class Chunk(BaseModel):
    chunk_id: str
    text: str
    section: str
    metadata: Dict[str, Any]
    entities: Dict[str, Any] = Field(default_factory=dict)
    relationships: List[Dict[str, Any]] = Field(default_factory=list)
    facts: List[Dict[str, Any]] = Field(default_factory=list)