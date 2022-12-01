from os import environ

import openai
from fastapi import HTTPException
from odmantic import AIOEngine

from young_tista.api.models.mongo import Question


class Questions:
    @classmethod
    async def ask_question(cls, engine: AIOEngine, question: str, temperature: float = 0.7):
        openai.api_key = environ.get("OPENAI_API_KEY")

        with open('model.txt', 'r') as f:
            prompt = f.read()
            prompt += f"{question}\n"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=750,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        choices = response.get('choices')
        if len(choices) == 0:
            raise HTTPException(status_code=400, detail="Bad question")

        choice = choices[0]
        text = choice.get('text').replace('Young Tista:\n', '').replace('Young Tista:', '').strip()

        question = Question(question=question, answer=text, gpt_response=response)
        await engine.save(question)

        return question
