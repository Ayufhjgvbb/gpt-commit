import click
from . import generator


@click.command()
@click.option(
    "--backend",
    type=click.Choice(["openai", "ollama"], case_sensitive=False),
    default="ollama",
    help="LLM backend to use.",
)
@click.option(
    "--commit", is_flag=True, help="Automatically commit with the generated message."
)
@click.option(
    "--model", default="codellama:latest", help="Model name (OpenAI or Ollama)."
)
def main(backend, commit, model):
    if commit:
        generator.direct_commit(backend, model)
    
