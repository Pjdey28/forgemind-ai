
from parsers.base_parser import BaseParser
class TXTParser(BaseParser):
    def parse(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()