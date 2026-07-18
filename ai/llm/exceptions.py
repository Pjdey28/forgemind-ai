class LLMException(Exception):
    """Base LLM Exception"""


class LLMResponseException(LLMException):
    """Invalid response received"""


class LLMConnectionException(LLMException):
    """Groq connection failed"""