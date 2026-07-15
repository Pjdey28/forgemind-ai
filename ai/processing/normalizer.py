import unicodedata


class TextNormalizer:

    @staticmethod
    def normalize(text: str):

        return unicodedata.normalize("NFKC", text)