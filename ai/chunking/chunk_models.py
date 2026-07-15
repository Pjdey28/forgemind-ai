from pydantic import BaseModel
from typing import Dict, Any


class Chunk(BaseModel):

    chunk_id: str

    text: str

    section: str

    metadata: Dict[str, Any]