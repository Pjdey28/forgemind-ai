from parsers.base_parser import BaseParser
from ocr.easyocr_engine import EasyOCREngine

class ImageParser(BaseParser):
    _ocr_engine = None

    def __init__(self):
        if ImageParser._ocr_engine is None:
            ImageParser._ocr_engine = EasyOCREngine()

    def parse(self, file_path: str) -> str:
        return ImageParser._ocr_engine.extract(file_path)