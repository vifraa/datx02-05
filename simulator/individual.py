import math
import datetime


class Individual:

    def __init__(self, birth= datetime.date(1, 1, 1), gender="", name="", bench_press_movement=0, path_to_csv=""):
        if(path_to_csv == ""):
            self.birth = birth
            self.gender = gender
            self.name = name
            self.bench_press_movement = bench_press_movement
        else:
            load_CSV(path_to_csv)

    def getAge(self, date: datetime):
        return math.floor((date - self.birth).days/365)

    def load_CSV(self, path_to_csv):
        return

    def save_to_CSV(self, path_to_save):
        return
