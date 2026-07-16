from pydantic import BaseModel, Field
from typing import Dict, Any
from datetime import datetime

class DocumentSchema(BaseModel):
    filename: str
    filetype: str
    text: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    processed_at: datetime = Field(default_factory=datetime.utcnow)