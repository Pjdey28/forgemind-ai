import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:
        text = text.replace("\x00", "")
        text = text.replace("\t", " ")
        text = re.sub(r"\s+", " ", text)
        return text.strip()