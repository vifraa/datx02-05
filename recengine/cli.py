"""
Module containing the CLI application for the Recommendation Engine.
"""
import json
import pprint
import click
import numpy as np
from recengine import RecommendationEngine

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
@click.option('--weight', '-w', prompt=True, required=True, type=float)
@click.option('--performance', '-p', prompt=True, required=True, type=float)
@click.option('--sex', type=click.Choice(['MAN', 'WOMAN', 'OTHER'], case_sensitive=False),
              prompt=True, required=True)
def pbar(age, weight, performance, sex):
    """
    Makes recommendation based on performance before the training program.
    """
    if sex == 'MAN':
        converted_sex = 0
    elif sex == 'WOMAN':
        converted_sex = 1
    else:
        converted_sex = 2

    data = np.array([age, weight, converted_sex, performance]).reshape(1, -1)
    recengine = RecommendationEngine("pbar")
    best_pred, _ = recengine.recommend_training(data)

    click.echo("\n")
    click.echo("Predicted performance: " + str(best_pred["predicted_performance"]))
    click.echo("Training program: " + best_pred["model"].name + "\n")
    click.echo("(Used model): " + str(best_pred["model"].__dict__))
