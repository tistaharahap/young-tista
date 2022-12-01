from asyncer import asyncify
from odmantic import AIOEngine

from young_tista.api.models.mongo import Question
from young_tista.ask import ask_young_tista


class Questions:
    @classmethod
    async def ask_question(cls, engine: AIOEngine, question: str, temperature: float = 0.7):
        text, response = await asyncify(ask_young_tista)(question=question, temperature=temperature)

        question = Question(question=question, answer=text, gpt_response=response)
        await engine.save(question)

        return question
