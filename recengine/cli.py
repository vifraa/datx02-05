"""
Module containing the CLI application for the Recommendation Engine.
"""
import json
import pprint
import click
import numpy as np
from recengine import RecommendationEngine, fetch_program_from_model

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
@click.option('--hideprogram', '-h', is_flag="True")
def pbar(age, weight, performance, sex, hideprogram):
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
    program = fetch_program_from_model(best_pred["model"])

    click.secho("\nTraining program: " + best_pred["model"].name, fg="green")
    click.secho("Predicted performance: " +
                str(best_pred["predicted_performance"]) + "\n", fg="green")

    hide_program_output = hideprogram
    if hide_program_output is False:
        click.secho("Program structure: ", fg="green")
        for day, sets in program.items():
            click.secho("Day: " + str(day), fg="green")
            for i, p_set in enumerate(sets):
                calculated_weight = (float(p_set[1]) / 100 * performance)
                click.secho("     (Set " + str(i) + ") Weight: " +
                            str(calculated_weight) + " Reps: " + str(p_set[2]))
