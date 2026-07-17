import pdfplumber
from parsers.base_parser import BaseParser

class PDFParser(BaseParser):
    def parse(self, file_path: str) -> str:
        text_content = []
        
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                # 1. Extract standard text
                text = page.extract_text()
                if text:
                    text_content.append(text)
                
                # 2. Extract structural tables and convert to Markdown
                tables = page.extract_tables()
                for table in tables:
                    if table and len(table) > 1:
                        # Clean up line breaks inside table cells
                        clean_table = [[str(cell).replace('\n', ' ') if cell else "" for cell in row] for row in table]
                        
                        # Build Markdown Table
                        headers = clean_table[0]
                        md_table = "\n| " + " | ".join(headers) + " |\n"
                        md_table += "|" + "|".join(["---" for _ in headers]) + "|\n"
                        
                        for row in clean_table[1:]:
                            # Pad row to match header length to prevent broken markdown
                            padded_row = row + [""] * (len(headers) - len(row))
                            md_table += "| " + " | ".join(padded_row[:len(headers)]) + " |\n"
                            
                        text_content.append(md_table)
                        
        return "\n".join(text_content)