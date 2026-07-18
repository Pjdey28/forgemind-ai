from pathlib import Path
from datetime import datetime

def build_metadata(file_path: str) -> dict:
    path = Path(file_path)
    return {
        "filename": path.name,
        "extension": path.suffix.lower(),
        "size": path.stat().st_size if path.exists() else 0,
        "created": datetime.utcnow().isoformat()
    }