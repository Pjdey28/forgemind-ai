from pathlib import Path
from datetime import datetime


def build_metadata(file_path: str):

    path = Path(file_path)

    return {
        "filename": path.name,
        "extension": path.suffix.lower(),
        "size": path.stat().st_size,
        "created": datetime.now().isoformat()
    }