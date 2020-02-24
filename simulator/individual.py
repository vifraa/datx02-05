import math
import datetime
import pandas as pd
import pickle


class Individual:

    def __init__(self, id="", birth: datetime = datetime.date(1, 1, 1), gender=2, name="", weight = 0, bench_press_movement=0, path_to_csv=""):
        if(path_to_csv == ""):
            self.birth = birth
            self.gender = gender
            self.name = name
            self.weight = weight
            self.id = id
            self.bench_press_movement = bench_press_movement
        else:
            self.load_CSV(path_to_csv)

    def getAge(self, date: datetime):
        return math.floor((date - self.birth).days/365)

    def load_CSV(self, path_to_csv):
        df = pd.read_csv(path_to_csv)
        dfRow = df.loc[df['id'] == self.id]
        self.birth = datetime.strptime(dfRow['birth'],'%Y-%m-%d')
        self.gender = dfRow['gender']
        self.name = dfRow['name']
        self.weight = dfRow['weight']


    def to_dataframe(self):
        dic = {'id': [self.id],'birth': [self.birth],'gender': [self.gender],'name': [self.name], 'weight': [self.weight],'bench_press_movement': [pickle.dumps(self.bench_press_movement)]}
        return pd.DataFrame(dic)
