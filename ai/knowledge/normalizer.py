import re


class KnowledgeNormalizer:

    def normalize_name(self, value: str):

        value = value.strip()

        value = re.sub(r"\s+", " ", value)

        value = value.replace("-", " ")

        return value.title()