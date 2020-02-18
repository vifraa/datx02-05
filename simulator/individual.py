import math


class Individual:

    def __init__(self, age=0, gender="", name="", fitness=1, fatique=1, performance=1, path_to_csv=""):
        if(path_to_csv == ""):
            self.age = age
            self.gender = gender
            self.name = name
            self.fitness = fitness
            self.fatique = fatique
            self.performance = performance
        else:
            load_CSV(path_to_csv)

    def fitness_decay(self):
        return 1

    def fatique_decay(self):
        return 1

    def fitness_gain(self):
        return 1

    def fatique_gain(self):
        return 1

    def amrap(self, weight):
        return math.floor(30 * (performance/weight - 1))

    def load_CSV(self, path_to_csv):
        return

    def save_to_CSV(self, path_to_save):
        return
