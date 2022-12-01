import typer

from young_tista.ask import ask_young_tista

app = typer.Typer()


@app.command()
def ask(
    question: str = typer.Option(None, prompt=True),
    temperature: float = typer.Option(0.7, help="Temperature of the model"),
):
    text = ask_young_tista(question=question, temperature=temperature)
    print(f"Young Tista: {text}")


if __name__ == "__main__":
    app()
