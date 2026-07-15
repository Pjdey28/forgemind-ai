from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime


class DocumentSchema(BaseModel):
    filename: str
    filetype: str
    text: str
    metadata: Dict[str, Any]
    processed_at: datetime