import math

class Movement:

    def __init__(self, fitness, fatigue, performance, fitness_gain, fatigue_gain, fitness_decay, fatigue_decay):
        self.fitness       = fitness
        self.fatigue       = fatigue
        self.performance   = performance

        self.fitness_gain  = fitness_gain
        self.fatigue_gain  = fatigue_gain

        self.fitness_decay = fitness_decay
        self.fatigue_decay = fatigue_decay

    def amrap(self, weight):
        reps = math.floor(30 * (self.performance/weight - 1))
        return max(0, reps)
