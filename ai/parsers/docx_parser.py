from docx import Document

from parsers.base_parser import BaseParser


class DOCXParser(BaseParser):

    def parse(self, file_path):

        doc = Document(file_path)

        paragraphs = []

        for para in doc.paragraphs:
            paragraphs.append(para.text)

        return "\n".join(paragraphs)