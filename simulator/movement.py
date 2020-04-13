"""Module contains class to simulate Banister model parameters for a given movement."""

import math


class Movement:
    """The Movement class should be used for each of the interesting movements in powerlifting, i.e.
    the squat, bench press and deadlift. The parameters of the Movement class are those which are
    relevant to the Banister model."""

    def __init__(self, fitness, fatigue, basic_performance, fitness_gain, fatigue_gain, fitness_decay,
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
        self.basic_performance = basic_performance

        self.fitness_gain = fitness_gain
        self.fatigue_gain = fatigue_gain

        self.fitness_decay = fitness_decay
        self.fatigue_decay = fatigue_decay

        self.last_performed_set = None
        self.current_PC_percentage = 1

    def get_current_performance(self):
        """Uses the definition of the performance from the difference between the current levels
        of fitness and fatigue from the Banister model.

        :returns: number denoting current level of performance in terms of 1RM

        """
        return self.basic_performance + self.fitness_gain * self.fitness \
            - self.fatigue_gain * self.fatigue

    def amrap(self, weight):
        """Uses Mayhew's formula to calculate how many reps an individual can perform at a given
        weight in a single set. NOTE: The equation is only accurate up to 11 reps. This means
        that to keep things reasonable the range for this function is only up to 75% intensity
        or 11 rep AMRAPs.

        :param weight: Amount of weight to use in the set.
        :returns: The amount of reps possible to perform using the given weight in a set.

        """
        intensity = weight/self.get_current_performance()
        if 0.91 < intensity <= 1:
            return 1
        elif intensity < 0.70:
            return 15
        else:
            reps = math.floor((math.log(41.9) -
                               math.log(100*weight/self.get_current_performance() - 52.2))/.055)
        return max(0, reps)

    def set_reps_performed(self, reps_performed, reps_possible):
        """Updates the current PC-percentage after some reps where performed.

        :param reps_performed: Amount of repetitions performed.
        :param reps_possible: Amount of repetitions that potentially could be performed until failure.

        """

        if reps_possible > 0:
            self.current_PC_percentage = self.current_PC_percentage * \
                (1 - (reps_performed/reps_possible))

    def get_PC_recovered_percentage(self, timestamp):
        """Uses the timestamp of the current set and subtracts from 
        the last performed set, which gives the rest time between the set. Uses 30 seconds as half-time for the 
        phosphorylcreatine (PC) levels. 
        Used publication: "The Time Course of Phosphorylcreatine Resynthesis during Recovery of the Quadriceps Muscle in Man"

        :param timestamp: The timestamp of the next set that is going to be performed.

        """
        if(self.last_performed_set is not None):
            rest_time = timestamp - self.last_performed_set
            self.last_performed_set = timestamp
            self.current_PC_percentage = (
                1 - (1 - self.current_PC_percentage)*pow(0.5, rest_time.seconds/30))
            return self.current_PC_percentage
        else:
            self.last_performed_set = timestamp
            return 1
