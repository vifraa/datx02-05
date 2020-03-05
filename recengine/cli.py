import click

@click.group()
def cli():
    """Recengine is the CLI interface for working with the training recommendation engine.
    """


@cli.command()
def hello():
    """Says hello to the world."""
    click.echo("Hello World")



