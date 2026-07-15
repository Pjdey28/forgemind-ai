from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME")

    TEMPERATURE = float(os.getenv("TEMPERATURE", 0))

    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 4096))

    CHROMA_DB = os.getenv("CHROMA_DB")

    NEO4J_URI = os.getenv("NEO4J_URI")

    NEO4J_USER = os.getenv("NEO4J_USER")

    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


settings = Settings()