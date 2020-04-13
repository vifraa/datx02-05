"""Module contains class representing a powerlifting trainee for use during the simulation of
powerlifting training."""

import math
from datetime import datetime
import pandas as pd
from movement import Movement


class Individual:
    """The Individual class is representing an individual with several personal parameters."""

    def __init__(self, id="", birth: datetime = datetime(1, 1, 1), name="",
                 bench_press_movement=None, series=pd.Series()):
        """Constructor for the indivual class

        :param id: An unique identifier.
        :param name: The individual's name.
        :param bench_press_movement: An instance of Movement representing benchpress.
        :param series: Makes it possible to load an individual from an one-dimentional array (series).
        """
        if series.empty:
            self.name = name
            self.id = id
            self.bench_press_movement = bench_press_movement
        else:
            self.load_from_series(series)

    def load_from_series(self, series):
        """Loads an individual from a given one-dimentional array (series).

        :param series: The one-dimentional array (series) that the individual will be initialized from.
        """
        self.id = series['ID']
        self.name = series['Name']
        self.bench_press_movement = Movement(
            series["bench_press_fitness"],
            series["bench_press_fatigue"],
            series["bench_press_basic_performance"],
            series["bench_press_fitness_gain"],
            series["bench_press_fatigue_gain"],
            series["bench_press_fitness_decay"],
            series["bench_press_fatigue_decay"],
        )

    def to_series(self):
        """Returns an one-dimentional array (series) containing all parameters from the individual."""

        series = {
            'ID': self.id, 'Name': self.name,
            'bench_press_fitness': self.bench_press_movement.fitness,
            'bench_press_fatigue': self.bench_press_movement.fatigue,
            'bench_press_basic_performance': self.bench_press_movement.get_current_performance(),
            'bench_press_fitness_gain': self.bench_press_movement.fitness_gain,
            'bench_press_fatigue_gain': self.bench_press_movement.fatigue_gain,
            'bench_press_fitness_decay': self.bench_press_movement.fitness_decay,
            'bench_press_fatigue_decay': self.bench_press_movement.fatigue_decay,
        }
        return pd.Series(series)
