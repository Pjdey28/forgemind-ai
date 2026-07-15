import os


class MetadataExtractor:

    @staticmethod
    def extract(document):

        return {

            "filename": os.path.basename(document.file_path),

            "extension": document.file_path.split(".")[-1].lower(),

            "pages": getattr(document, "pages", None),

            "source": "upload"

        }