"""Module contains class to simulate Banister model parameters for a given movement."""

import math


class Movement:
    """The Movement class should be used for each of the interesting movements in powerlifting, i.e.
    the squat, bench press and deadlift. The parameters of the Movement class are those which are
    relevant to the Banister model."""

    def __init__(self, fitness, fatigue, performance, fitness_gain, fatigue_gain, fitness_decay,
                 fatigue_decay):
        """Constructor for the Movement class.

        :param fitness: Initial level of fitness in the movement.
        :param fatigue: Initial level of fatigue in the movement.
        :param performance: Initial level of performance (1RM) in the movement.
        :param fitness_gain: A factor denoting the positive contribution of a given load on current
        performance.
        :param fatigue_gain: A factor denoting the negative contribution of a given load on current
        performance.
        :param fitness_decay: Denotes how quickly the positive component of performance dissipates.
        :param fatigue_decay: Denotes how quickly the negative component of performance dissipates.
        """
        self.fitness = fitness
        self.fatigue = fatigue
        self.performance = performance

        self.fitness_gain = fitness_gain
        self.fatigue_gain = fatigue_gain

        self.fitness_decay = fitness_decay
        self.fatigue_decay = fatigue_decay

    def amrap(self, weight):
        """Uses Epley's formula to calculate how many reps an individual can perform at a given
        weight in a single set.

        :param weight: Amount of weight to use in the set.
        :returns: The amount of reps possible to perform using the given weight in a set.

        """
        reps = math.floor(30 * (self.performance / weight - 1))
        return max(0, reps)
