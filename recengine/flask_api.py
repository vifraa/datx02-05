from flask import Flask, request, jsonify, render_template
from recengine import RecommendationEngine
import numpy as np


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

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
        best_pred, all_predictions = recengine.recommend_training(data)

        res = {
            "predicted_performance": best_pred["predicted_performance"],
            "training_program": best_pred["model"].name,
            "all_predictions": all_predictions
        }

        return jsonify(res)


    return f"{performance}{weight}{sex}{age}"





if __name__ == "__main__":
    app.run(debug=True)
