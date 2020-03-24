from flask import Flask, request
from recengine import RecommendationEngine
import numpy as np


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route('/pbar', methods = ['GET', 'POST'])
def pbar():
    if request.method == 'GET':
        return "GET"

    elif request.method == 'POST':
        recengine = RecommendationEngine("pbar")
        age = int(request.args.get('age', ''))
        weight = float(request.args.get('weight',''))
        sex = request.args.get('sex','')
        performance = float(request.args.get('performance',''))
        if sex == 'MAN':
            converted_sex = 0
        elif sex == 'WOMAN':
            converted_sex = 1
        else:
            converted_sex = 2
        data = np.array([age, weight, converted_sex, performance]).reshape(1, -1)
        best_pred, _ = recengine.recommend_training(data)
    return f"{performance}{weight}{sex}{age}"





if __name__ == "__main__":
    app.run(debug=True)