"""This is the main interface to the simulator package. The simulator package provides functionality
for generating virtual powerlifting trainees and a virtual environment in which these trainees can
train. The training effects of performing the training can then be observed and logged, and the
individuals themselves (along with their personal attributes) can be logged as well."""
import threading
import pandas as pd
import gym
from generator import generate_individuals, save_individuals
from individual import Individual
import click
import os
import random


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

    print(training_logs)
    # write training logs to given file path
    training_logs.to_csv(training_results_path, sep="|", index=False)

    return training_logs["Timestamp"].iloc[-1]


def __train_and_save_in_parallel(individuals, training_results_path, training_program_path):
    """
    Trains the individuals with the given traning program in parallel and save the logs

    :param individuals: Individuals to train
    :param training_results_path: Path to save logs to
    :param training_program_path: Path to training program

    :returns: Timestamp of the last completed workout

    """
    # If the number of individuals is more than the limit then one thread will be
    # created for each 100 individuals to handle their data in parallel
    LIMIT = 100

    # creating training_logs_list and defining number_of_threads
    column_names = ["ID", "Exercise", "Weight", "Reps", "Timestamp"]
    number_of_threads = int(len(individuals)/LIMIT)
    training_logs_list = [pd.DataFrame(columns=column_names) for _ in range(number_of_threads)]

    # nested method to perform the training
    def perform_training(index, _from, _to):
        # perform training
        for individual in individuals[_from:_to]:
            training_dataframe = gym.load_training(
                training_program_path, individual.bench_press_movement)
            performed_training = gym.train(training_dataframe, individual)
            performed_training.insert(
                0, "ID", [individual.id] * performed_training.shape[0], True)
            training_logs_list[index] = training_logs_list[index].append(performed_training)

    # get the bounds that the worker thread will work between
    def get_from_to(index, offset, length):
        if index >= (length - offset):
            return index, length
        else:
            return index, offset + index

    thread_list = []
    offset = 0
    threading_index = 0

    # creating threads in thread_list
    while offset < len(individuals):
        _from, _to = get_from_to(offset, LIMIT, len(individuals))
        thread_list.append(threading.Thread(target=perform_training, args=[threading_index, _from, _to]))
        offset += LIMIT
        threading_index += 1

    # starting and joining threads
    [worker.start() for worker in thread_list]
    [worker.join() for worker in thread_list]

    column_names = ["ID", "Exercise", "Weight", "Reps", "Timestamp", "Performance"]
    training_logs_t = pd.DataFrame(columns=column_names)
    training_logs = pd.DataFrame(columns=column_names)
    for sublist in training_logs_list:
        if training_logs_t.empty:
            training_logs_t = pd.DataFrame(sublist, columns=column_names)
            training_logs = pd.DataFrame(sublist, columns=column_names)
        else:
            training_logs_t = training_logs
            sublist_df = pd.DataFrame(sublist)
            training_logs = training_logs_t.append(sublist_df)

    training_logs = training_logs.sort_values('ID')
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

    if len(individuals) < 100:
        timestamp = __train_and_save(
            individuals, training_results_path, training_program_path)
        save_individuals(individuals, individuals_path, timestamp)
    else:
        timestamp2 = __train_and_save_in_parallel(
            individuals, training_results_path, training_program_path)
        save_individuals(individuals, individuals_path, timestamp2)




def train_population_from_file_random_program(individuals_path, programs_dict, training_results_path):
    """Takes a file containing a set of individuals to expose training to. The function then saves
    these individuals and their training data in a csv file.

    :param individuals_path: file path to folder containing training individuals csv files
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

        # Get a random program
        training_program_path = programs_dict[random.randint(
            1, len(programs_dict))]
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
    click.echo(f"{count}: Random program for each individual")
    click.echo(f"{count+1}: No pre-training program")
    pre_training_num = click.prompt(
        'Please enter the number of the program to train before', type=int)

    # If user selected last number, we choose random
    random_pre_program = count == pre_training_num
    no_pre_program = count+1 == pre_training_num
    training_num = click.prompt(
        'Please enter the number of the program to train', type=int)
    training_program = programs_map_to_id[training_num]
    if not no_pre_program:
        if random_pre_program:
            train_population_from_file_random_program(
                "simulator/individuals/GeneratedIndividuals.csv", programs_map_to_id, "simulator/output/pre_program_logs.csv")
        else:
            pre_training_program = programs_map_to_id[pre_training_num]
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
