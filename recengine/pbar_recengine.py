import os
from recengine import load_models, make_prediction

class PbarRecengine:

    def __init__(self):
        dir_path = os.path.join(os.path.dirname(__file__), "pbar")
        self.models = load_models(dir_path)


    def recommend_training(self, individual, preperformance: float):
        data = {individual, preperformance}
        print(data)
        return make_prediction(self.models, data)




