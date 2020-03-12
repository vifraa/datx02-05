import click
from pbar_recengine import PbarRecengine

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
def pbar(age, weight, performance, sex):
    """
    Based on individuals parameters recommend what training program will bring the most gains.
    """
    data = {"age": age, "weight": weight, "sex": sex}
    recengine = PbarRecengine()
    pred = recengine.recommend_training(data, performance)

    click.echo("Worked")
    click.echo(pred)
