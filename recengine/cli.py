import click
from recengine import recommend_training

@click.group()
def cli():
    """Recengine is the CLI interface for working with the training recommendation engine.
    """


@cli.command()
def hello():
    """Says hello to the world."""
    click.echo("Hello World")


@cli.command()
@click.option('--age', '-a', prompt=True, required=True, type=int)
@click.option('--weight', '-w', prompt=True, required=True, type=int)
@click.option('--performance', '-p', prompt=True, required=True, type=float)
@click.option('--sex', type=click.Choice(['MAN', 'WOMAN'], case_sensitive=False),
              prompt=True, required=True)
def recommend(age, weight, performance, sex):
    """
    Recommends training based on the given parameters.
    """
    
    click.echo("Worked")
