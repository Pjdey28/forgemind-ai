import json
from groq import Groq

from config.settings import settings


class GroqClient:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.model = settings.GROQ_MODEL

    def generate(

        self,

        prompt: str,

        system_prompt: str | None = None,

        temperature: float = 0.2

    ) -> str:

        messages = []

        if system_prompt:

            messages.append({

                "role": "system",

                "content": system_prompt

            })

        messages.append({

            "role": "user",

            "content": prompt

        })

        response = self.client.chat.completions.create(

            model=self.model,

            messages=messages,

            temperature=temperature

        )

        return response.choices[0].message.content

    def generate_json(

        self,

        prompt,

        system_prompt

    ):

        response = self.generate(

            prompt,

            system_prompt

        )

        return json.loads(response)