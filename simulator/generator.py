import numpy as np
import names
#from individual import Individual

def generate_indviduals(num, age_mean, age_variance, bench_press_fitness_mean, bench_press_fitness_variance):
    '''
    Generates individuals to be used in the simulator

    :param num: Number of individuals to generate.
    :param age_mean: The mean of the age for the individuals
    :param age_variance: The variance in age for the individuals for a normal distribution
    :param bench_press_fitness_mean: The mean of the 1RM in bench press for the individuals
    :param bench_press_fitness_variance: The variance in the 1RM for the individuals for a normal distribution
    :return: A list of individuals generated
    '''

    individuals = []
    ages = np.random.normal(age_mean, age_variance, num).astype("int")
    bench_press_fitnesses = np.random.normal(bench_press_fitness_mean, bench_press_fitness_variance, num).astype("int")
    for i in range(num):
        name = names.get_full_name()
        individuals.append([name, ages[i], bench_press_fitnesses[i]])
    return individuals

def save_individuals(individuals):
    '''
    Saves all individuals  blabla
    '''
    pass


if __name__ == "__main__":
    print(generate_indviduals(50,30,5,100,5))

