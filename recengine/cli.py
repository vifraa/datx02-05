"""
Module containing the CLI application for the Recommendation Engine.
"""
import json
import os
import pprint
import click
import numpy as np
from recengine import RecommendationEngine, fetch_program_from_model
from data_parser import ttrdata_from_csv

@click.group()
def cli():
    """Recengine is the CLI interface for working with the training recommendation engine.
    """


def print_training_program_from_model(model, performance):
    """
    Prints the training program related to the given model.

    :param model: Model to find program from.
    :param performance: Current performance of the individual.
    """
    program = fetch_program_from_model(model)



    click.secho("Program structure: ", fg="green")
    for day, sets in program.items():
        click.secho("Day: " + str(day), fg="green")
        for i, p_set in enumerate(sets):
            calculated_weight = (p_set.percent_1rm / 100 * performance)
            click.secho("     (Set " + str(i) + ") Weight: " +
                        str(calculated_weight) + " Reps: " + str(p_set.repetitions))




@cli.command()
@click.option('--age', '-a', prompt=True, required=True, type=int)
@click.option('--weight', '-w', prompt=True, required=True, type=float)
@click.option('--performance', '-p', prompt=True, required=True, type=float)
@click.option('--sex', type=click.Choice(['MAN', 'WOMAN', 'OTHER'], case_sensitive=False),
              prompt=True, required=True)
@click.option('--hideprogram', '-h', is_flag="True",
              help="Hide the output of the program structure.")
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

    click.secho("\nTraining program: " + best_pred["model"].name, fg="green")
    click.secho("Predicted performance: " +
                str(best_pred["predicted_performance"]) + "\n", fg="green")

    if hideprogram is False:
        print_training_program_from_model(best_pred["model"], performance)

@cli.command()
@click.option('--file', '-f', required=True, type=str, help="Filepath to training data csv.")
@click.option('--timeformat', '-t', prompt=True, required=True, type=str, 
              help="Time format of the timestamp column.")
@click.option('--hideprogram', '-h', is_flag="True",
              help="Hide the output of the program structure.")
def ttr(file, timeformat, hideprogram):
    """
    Using previous training data makes an recommendation.

    Format of the CSV file should be the following with '|' delimiters:
    Exercice | Weight | Reps | Timestamp
    """

    full_path = os.path.join(os.getcwd(), file)
    ttrdata = ttrdata_from_csv(full_path, timeformat)

    click.echo(str(ttrdata))
    click.echo(full_path)


#    if hideprogram is False:
#        print_training_program_from_model(best_pred["model"], performance)
