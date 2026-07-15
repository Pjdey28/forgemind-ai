import pandas as pd

from parsers.base_parser import BaseParser


class ExcelParser(BaseParser):

    def parse(self, file_path):

        excel = pd.ExcelFile(file_path)

        text = ""

        for sheet in excel.sheet_names:

            df = excel.parse(sheet)

            text += df.to_string()

            text += "\n"

        return text