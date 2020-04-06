"""This is the main interface to the simulator package. The simulator package provides functionality
for generating virtual powerlifting trainees and a virtual environment in which these trainees can
train. The training effects of performing the training can then be observed and logged, and the
individuals themselves (along with their personal attributes) can be logged as well."""

import pandas as pd
import gym
from generator import generate_individuals, save_individuals
from individual import Individual
import click
import os


def __train_and_save(individuals, training_results_path, training_program_path):
    """
    Trains the individuals with the given traning program and save the logss

    :param individuals: Individuals to train
    :param training_results_path: Path to save logs to
    :param training_program_path: Path to training program


    :returns: Timestamp of the last completed workout

    """
    column_names = ["ID", "Exercise", "Weight", "Reps", "Timestamp"]
    training_logs = pd.DataFrame(columns=column_names)

    # load training program

    # perform training
    for individual in individuals:
        training_dataframe = gym.load_training(
            training_program_path, individual.bench_press_movement)
        performed_training = gym.train(training_dataframe, individual)
        performed_training.insert(
            0, "ID", [individual.id] * performed_training.shape[0], True)
        training_logs = training_logs.append(performed_training)

    # write training logs to given file path
    training_logs.to_csv(training_results_path, sep="|", index=False)

    return training_logs["Timestamp"].iloc[-1]


def train_population(population_size, age_mean, age_variance, weight_mean, weight_variance,
                     bench_press_fitness_mean, bench_press_fitness_variance, gender_ratio,
                     training_program_path, training_results_path, individuals_path):
    """Takes a set of population parameters and generates a population. These individuals are then
    exposed to a given training program. The function then saves these individuals and their
    training data in a csv file.

    :param population_size: Number of individuals to generate.
    :param age_mean: The mean of the age for the individuals
    :param age_variance: The variance in age for the individuals for a normal distribution
    :param bench_press_fitness_mean: The mean of the 1RM in bench press for the individuals
    :param bench_press_fitness_variance: The variance in the 1RM for the individuals for a normal
    distribution
    :param gender_ratio: The ratio of individuals with female sex characteristics
    :param training_program_path: Path to training program
    :param training_results_path: File path to where performed training should be saved as csv file
    :param individuals_path: File path to where the generated individuals should be saved

    """

    individuals = generate_individuals(population_size, age_mean, age_variance, weight_mean,
                                       weight_variance, bench_press_fitness_mean,
                                       bench_press_fitness_variance, gender_ratio)
    timestamp = __train_and_save(
        individuals, training_results_path, training_program_path)

    # save the generated individuals
    save_individuals(individuals, individuals_path, timestamp)


def train_population_from_file(individuals_path, training_program_path, training_results_path):
    """Takes a file containing a set of individuals to expose training to. The function then saves
    these individuals and their training data in a csv file.

    :param individuals_path: file path to folder containing training individuals csv files
    :param training_program_path: file path to prescribed training program
    :param training_results_path: file path to where performed training should be saved as csv file

    """

    # load individuals from csv file
    individuals_df = pd.read_csv(individuals_path, sep="|")
    individuals_df = individuals_df.sort_values('Timestamp').drop_duplicates(
        ['ID'], keep='last')
    # construct objects from entries
    individuals = []
    for _, individual_series in individuals_df.iterrows():
        individuals.append(Individual(series=individual_series))

    timestamp = __train_and_save(
        individuals, training_results_path, training_program_path)

    # add the updated individuals to bottom of csv file
    save_individuals(individuals, individuals_path, timestamp)


@click.command()
def choose_programs():
    """
    Allows the user to choose which program was trained before and which program to 'actually' train.
    """
    PROGRAMS_DIR = os.path.join("simulator", "training_programs")
    programs_map_to_id = {}
    count = 1
    click.echo("Programs:")
    for fn in os.listdir(PROGRAMS_DIR):
        programs_map_to_id[count] = os.path.join(PROGRAMS_DIR, fn)
        click.echo(f"{count}: {fn}")
        count += 1

    pre_training_program = programs_map_to_id[click.prompt(
        'Please enter the number of the program to train before', type=int)]
    training_program = programs_map_to_id[click.prompt(
        'Please enter the number of the program to train', type=int)]
    train_population_from_file("simulator/individuals/GeneratedIndividuals.csv",
                               pre_training_program, "simulator/output/pre_program_logs.csv")
    train_population_from_file("simulator/individuals/GeneratedIndividuals.csv",
                               training_program, "simulator/output/program_logs.csv")
    click.echo(
        "Your individuals were trained, results can be found in the output folder.")


if __name__ == "__main__":
    # train_population_from_file("simulator/individuals/GeneratedIndividuals.csv",
    # "simulator/tests/sample_training_program.csv", "simulator/individuals/logs.csv")
    # train_population(10, 30, 5, 70, 5, 100, 5, 1, "simulator/training_programs/ogasawara_HL.csv",
    #                 "simulator/individuals/logs.csv", "simulator/individuals/TrainedGeneratedIndividuals.csv")

    # train_population_from_file("simulator/individuals/GeneratedIndividuals.csv",
    #                           "simulator/training_programs/carls_power_program_BP.csv", "simulator/output/pre_program.csv")
    # train_population_from_file("simulator/individuals/GeneratedIndividuals.csv",
    #                          "simulator/training_programs/ogasawara_HL.csv", "simulator/output/ogasawara_HL.csv")

    # Clean up past output
    OUTPUT_DIR = os.path.join("simulator", "output")
    for fn in os.listdir(OUTPUT_DIR):

        # Skip hidden files
        if fn.startswith('.'):
            continue
        os.remove(os.path.join(OUTPUT_DIR, fn))

    click.echo(
        "Make sure you have generated a popuation using generator.py before running this!")
    choose_programs()
