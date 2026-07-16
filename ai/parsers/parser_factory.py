from parsers.pdf_parser import PDFParser
from parsers.docx_parser import DOCXParser
from parsers.excel_parser import ExcelParser
from parsers.image_parser import ImageParser
from parsers.txt_parser import TXTParser

class ParserFactory:

    @staticmethod
    def get_parser(extension):

        mapping = {

            ".pdf": PDFParser(),

            ".docx": DOCXParser(),

            ".xlsx": ExcelParser(),

            ".xls": ExcelParser(),

            ".png": ImageParser(),

            ".jpg": ImageParser(),

            ".jpeg": ImageParser(),
            ".txt": TXTParser()

        }

        parser = mapping.get(extension)

        if parser is None:
            raise ValueError("Unsupported document type")

        return parser