import re

class KnowledgeNormalizer:
    @staticmethod
    def normalize_id(value: str) -> str:
        return str(value).strip().upper()

    @staticmethod
    def normalize_relation(value: str) -> str:
        return str(value).strip().upper().replace(" ", "_")