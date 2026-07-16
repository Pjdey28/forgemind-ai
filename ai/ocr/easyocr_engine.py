import easyocr

class EasyOCREngine:
    def __init__(self):
        # Fallback thread-safe framework loader
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract(self, image_path: str) -> str:
        result = self.reader.readtext(image_path, detail=0)
        return "\n".join([str(line) for line in result])