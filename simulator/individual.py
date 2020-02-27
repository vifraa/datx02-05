import math
import datetime
import pandas as pd
import pickle


class Individual:

    def __init__(self, id="", birth: datetime = datetime.date(1, 1, 1), gender=2, name="", weight = 0, bench_press_movement=0, dataframe=None):
        if(dataframe == None):
            self.birth = birth
            self.gender = gender
            self.name = name
            self.weight = weight
            self.id = id
            self.bench_press_movement = bench_press_movement
        else:
            self.load_from_dataframe(dataframe)

    def getAge(self, date: datetime):
        return math.floor((date - self.birth).days/365)

    def load_from_dataframe(self, df):
        self.id = df['id']
        self.birth = datetime.strptime(df['birth'],'%Y-%m-%d')
        self.gender = df['gender']
        self.name = df['name']
        self.weight = df['weight']
        self.bench_press_movement = df['bench_press_movement']


    def to_dataframe(self):
        dic = {'id': [self.id],'birth': [self.birth],'gender': [self.gender],'name': [self.name], 'weight': [self.weight],'bench_press_movement': [pickle.dumps(self.bench_press_movement)]}
        return pd.DataFrame(dic)
