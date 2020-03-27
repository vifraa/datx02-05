"""Module contains class representing a powerlifting trainee for use during the simulation of
powerlifting training."""

import math
from datetime import datetime
import pandas as pd
from movement import Movement


class Individual:
    """The Individual class is representing an individual with several personal parameters."""

    def __init__(self, id="", birth: datetime = datetime(1, 1, 1), gender=2, name="", weight=0,
                 bench_press_movement=0, series=pd.Series()):
        """Constructor for the indivual class

        :param id: An unique identifier.
        :param birth: The individual's date of birth.
        :param gender: A number between 0-2 representing different genders.
        :param name: The individual's name.
        :param weight: The individual's weight in kilograms.
        :param bench_press_movement: An instance of Movement representing benchpress.
        :param series: Makes it possible to load an individual from an one-dimentional array (series).
        """
        if series.empty:
            self.birth = birth.date()
            self.gender = gender
            self.name = name
            self.weight = weight
            self.id = id
            self.bench_press_movement = bench_press_movement
        else:
            self.load_from_series(series)

    def get_age(self, date: datetime = datetime.now()):
        """Returns the individual's age at a given date.

        :param date: The end date in the subtraction of age.
        """
        return math.floor((date - self.birth).days / 365)

    def load_from_series(self, series):
        """Loads an individual from a given one-dimentional array (series).

        :param series: The one-dimentional array (series) that the individual will be initialized from.
        """
        self.id = series['ID']
        self.birth = datetime.strptime(series['Birth'], '%Y-%m-%d').date()
        self.gender = series['Gender']
        self.name = series['Name']
        self.weight = series['Weight']
        self.bench_press_movement = Movement(
            series["bench_press_fitness"],
            series["bench_press_fatigue"],
            series["bench_press_performance"],
            series["bench_press_fitness_gain"],
            series["bench_press_fatigue_gain"],
            series["bench_press_fitness_decay"],
            series["bench_press_fatigue_decay"],
        )

    def to_series(self):
        """Returns an one-dimentional array (series) containing all parameters from the individual."""

        series = {
            'ID': self.id, 'Birth': self.birth, 'Gender': self.gender, 'Name': self.name,
            'Weight': self.weight,
            'bench_press_fitness': self.bench_press_movement.fitness,
            'bench_press_fatigue': self.bench_press_movement.fatigue,
            'bench_press_performance': self.bench_press_movement.performance,
            'bench_press_fitness_gain': self.bench_press_movement.fitness_gain,
            'bench_press_fatigue_gain': self.bench_press_movement.fatigue_gain,
            'bench_press_fitness_decay': self.bench_press_movement.fitness_decay,
            'bench_press_fatigue_decay': self.bench_press_movement.fatigue_decay,
        }
        return pd.Series(series)
