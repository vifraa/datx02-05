import pandas as pd
import gym
import generator
from individual import Individual

def train_population(population_size, age_mean, age_variance, bench_press_fitness_mean, bench_press_fitness_variance,
                     gender_ratio, training_results_path):
    """Takes a set of population parameters and generates a population. These individuals are then exposed to
     a given training program. The function then saves these individuals and their training data in a csv file.

    :param num: Number of individuals to generate.
    :param age_mean: The mean of the age for the individuals
    :param age_variance: The variance in age for the individuals for a normal distribution
    :param bench_press_fitness_mean: The mean of the 1RM in bench press for the individuals
    :param bench_press_fitness_variance: The variance in the 1RM for the individuals for a normal distribution
    :param training_results_path: file path to where performed training should be saved as csv file

    """
    return None

def train_population_from_file(individuals_path, training_program_path, training_results_path):
    """Takes a file containing a set of individuals to expose training to. The function then saves these
    individuals and their training data in a csv file.

    :param individuals_path: file path to folder containing training individuals csv files
    :param training_program_path: file path to prescribed training program
    :param training_results_path: file path to where performed training should be saved as csv file

    """

    # load individuals from csv file
    individuals_df = pd.read_csv(individuals_path, sep="|")

    # construct objects from entries
    individuals = []
    for index, individual_series in individuals_df.iterrows():
        individuals.append(Individual(series=individual_series))

    column_names = ["ID", "Exercise", "Weight", "Reps", "Timestamp"]
    training_logs = pd.DataFrame(columns=column_names)

    # perform training
    for individual in individuals:
        performed_training = gym.train(training_program_path, individual)
        performed_training.insert(0, "ID", [individual.id] * performed_training.shape[0], True)
        training_logs = training_logs.append(performed_training)

    # write training logs to given file path
    training_logs.to_csv(training_results_path, sep="|", index=False)

if __name__ == "__main__":
    train_population_from_file("simulator/individuals/GeneratedIndividuals.csv", "simulator/tests/sample_training_program.csv",
                               "simulator/individuals/logs.csv")
