from parsers.base_parser import BaseParser

from ocr.easyocr_engine import EasyOCREngine


class ImageParser(BaseParser):

    def __init__(self):

        self.ocr = EasyOCREngine()

    def parse(self, file_path):

        return self.ocr.extract(file_path)