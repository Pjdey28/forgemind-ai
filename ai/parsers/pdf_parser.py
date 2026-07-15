import fitz

from parsers.base_parser import BaseParser


class PDFParser(BaseParser):

    def parse(self, file_path):

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        return text