from os import environ
from typing import Tuple

import openai


def ask_young_tista(question: str, temperature: float = 0.7) -> Tuple[str, dict]:
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
        raise ValueError("Bad question")

    choice = choices[0]

    return choice.get('text').replace('Young Tista:\n', '').replace('Young Tista:', '').strip(), response
