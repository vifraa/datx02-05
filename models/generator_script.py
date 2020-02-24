import math
import random
import csv
from datetime import datetime


def generate_individuals(individuals):
    mean = 50
    variance = 30
    starting_stength = [round(random.gauss(mean, math.sqrt(variance))) for i in range(individuals)]
    
    result = []
    for i, str in enumerate(starting_stength):
        person = Individual(i, str)
        result.append(person)

    return result

    
def generate_training(individual, sets):
    training_strength = individual.starting_stength
    result = []
    for _ in range(sets):
        kind_of_training = random.randint(1, 3)
        
        if (kind_of_training == 0):
            [result.append(Set(individual.id, 1, 3, round(training_strength * 0.9), training_strength)) for j in range(6)]
            training_strength = training_strength * random.uniform(1.009, 1.015)
        elif (kind_of_training == 1):
            [result.append(Set(individual.id, 1, 5, round(training_strength * 0.8), training_strength)) for j in range(5)]
            training_strength = training_strength * random.uniform(1.01, 1.02)
        elif (kind_of_training == 2):
            [result.append(Set(individual.id, 1, 8, round(training_strength * 0.75), training_strength)) for j in range(4)]
            training_strength = training_strength * random.uniform(1.005, 1.02)
        elif (kind_of_training == 3):
            [result.append(Set(individual.id, 1, 12, round(training_strength * 0.7), training_strength)) for j in range(4)]
            training_strength = training_strength * random.uniform(1.005, 1.012)
        elif (kind_of_training == 4):
            [result.append(Set(individual.id, 1, 15, round(training_strength * 0.55), training_strength)) for j in range(3)]
            training_strength = training_strength * random.uniform(1.003, 1.01)


    return result


class Individual:
    def __init__(self, id, starting_stength):
        self.id = id
        self.age = random.randint(18,50)
        self.weight = random.randint(60, 110)
        self.gender = random.randint(0,2)
        self.starting_stength = starting_stength
        self.timestamp = datetime.timestamp(datetime.now())

    def __str__(self):
        return "{id: " + str(self.id) + ", starting_stength: " + str(self.starting_stength) + "}"

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter([self.id, self.age, self.weight, self.gender, self.timestamp])

class Set: 
    def __init__(self, id, exercise, reps, weight, performance):
        self.id = id
        self.exercise = exercise
        self.reps = reps
        self.weight = weight
        self.performance = performance
        self.timestamp = datetime.timestamp(datetime.now())

    def __iter__(self):
        return iter([self.id, self.exercise, self.reps, self.weight, self.timestamp, self.performance])


individuals = generate_individuals(100)
result = []
for i in individuals:
    result.extend(generate_training(i, 200))


with open("training.csv", "w", newline="") as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    for v in result:
        wr.writerow(list(v))

with open("individuals.csv", "w", newline="") as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    for v in individuals:
        wr.writerow(list(v))
