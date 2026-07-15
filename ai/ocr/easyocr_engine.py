import easyocr


class EasyOCREngine:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['en'],
            gpu=False
        )

    def extract(self, image_path):

        result = self.reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)