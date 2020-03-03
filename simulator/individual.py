"""Module contains class representing a powerlifting trainee for use during the simulation of
powerlifting training."""

import math
from datetime import datetime
import pandas as pd
from movement import Movement


class Individual:

    def __init__(self, id="", birth: datetime = datetime(1, 1, 1), gender=2, name="", weight=0,
                 bench_press_movement=0, series=pd.Series()):
        if series.empty:
            self.birth = birth
            self.gender = gender
            self.name = name
            self.weight = weight
            self.id = id
            self.bench_press_movement = bench_press_movement
        else:
            self.load_from_series(series)

    def get_age(self, date: datetime = datetime.now()):
        return math.floor((date - self.birth).days / 365)

    def load_from_series(self, series):
        self.id = series['ID']
        self.birth = datetime.strptime(series['Birth'], '%Y-%m-%d')
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
