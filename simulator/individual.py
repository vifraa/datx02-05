import math
import datetime
import pandas as pd


class Individual:

    def __init__(self, birth: datetime = datetime.date(1, 1, 1), gender=2, name="", weight = 0, bench_press_movement=0, id="", path_to_csv=""):
        if(path_to_csv == ""):
            self.birth = birth
            self.gender = gender
            self.name = name
            self.weight = weight
            self.id = id
            self.bench_press_movement = bench_press_movement
        else:
            load_CSV(path_to_csv)

    def getAge(self, date: datetime):
        return math.floor((date - self.birth).days/365)

    def load_CSV(self, path_to_csv):
        df = pd.read_csv(path_to_csv)
        dfRow = df.loc[df['id'] == self.id]
        self.birth = datetime(dfRow['birth'])
        self.gender = dfRow['gender']
        self.name = dfRow['name']
        self.weight = dfRow['weight']


    def to_dataframe(self, path_to_save):
        dic = {'id': self.id,'birth': self.birth,'gender': self.gender,'name': self.name, 'weight': self.weight}
        columns = ['id','birth','gender','name','weight']
        return pd.DataFrame(dic,columns)
