import os
import openai

import typer

app = typer.Typer()


@app.command()
def ask(
    question: str = typer.Option(None, prompt=True),
    temperature: float = typer.Option(0.7, help="Temperature of the model"),
):
    openai.api_key = os.getenv("OPENAI_API_KEY")

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
    for choice in choices:
        text = choice.get('text').replace('Young Tista:\n', '').replace('Young Tista:', '').strip()
        print(f"Young Tista: {text}")
        print('\n')


if __name__ == "__main__":
    app()
