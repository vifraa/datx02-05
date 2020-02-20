import numpy as np
import names
from absl import flags
from absl import app
#from individual import Individual


FLAGS = flags.FLAGS

flags.DEFINE_integer("n",100,"How many individuals to generate")
flags.DEFINE_integer("bpm",100,"Mean of bench press max")
flags.DEFINE_integer("bpv",5,"Variance in bench press max")
flags.DEFINE_integer("am",30,"Age mean")
flags.DEFINE_integer("av",5,"Age variance")


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

def main(argv):
    generated_individuals = generate_indviduals(FLAGS.n, FLAGS.am, FLAGS.av, FLAGS.bpm, FLAGS.bpv)
    #save_individuals()

if __name__ == "__main__":
    app.run(main)
    #print(generate_indviduals(50,30,5,100,5))

