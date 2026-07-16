from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")  # Stable Groq production model
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.0))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 4096))
    CHROMA_DB = os.getenv("CHROMA_DB", "./chroma_db")
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "BAAI/bge-large-en-v1.5")

settings = Settings()