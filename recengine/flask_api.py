from flask import Flask, request, jsonify
from recengine import RecommendationEngine
import numpy as np


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"


@app.route('/pbar', methods=['POST'])
def pbar():

    recengine = RecommendationEngine("pbar")
    age = int(request.args.get('age', ''))
    weight = float(request.args.get('weight', ''))
    sex = request.args.get('sex', '')
    performance = float(request.args.get('performance', ''))
    if sex == 'MAN':
        converted_sex = 0
    elif sex == 'WOMAN':
        converted_sex = 1
    else:
        converted_sex = 2
    data = np.array([age, weight, converted_sex,
                     performance]).reshape(1, -1)
    best_pred, all_predictions = recengine.recommend_training(data)

    res = {
        "predicted_performance": best_pred["predicted_performance"],
        "training_program": best_pred["model"].name,
        "all_predictions": "lul"
    }

    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
