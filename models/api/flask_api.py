import io

from flask import Flask, jsonify,send_file, make_response
from flask_cors import CORS, cross_origin
import sys


sys.path.insert(1, 'C:/Users/razan/Desktop/Kandidatarbetet/datx02-05/models')
from visualizers.models_visual_training_comparator import Models_comparator
import ast
import MLmodels.DecisionTree as DecisionTree
import MLmodels.ElasticNets as ElasticNet
import MLmodels.Lasso as Lasso
import MLmodels.NeuralNetwork as NeuralNetwork
import MLmodels.RandomForest as RandomForest
import MLmodels.Ridge as Ridge
import MLmodels.LinearRegression as LinearRegression
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

last_used_model_name = ""
last_used_training_set = ""

@app.route("/")
def index():
    return 'Hello from  Models!'


@app.route("/models")
def model_names():
    res = [
        ["Linear Model", "Linear", "https://lh3.googleusercontent.com/proxy/TXzQC9Le_D21W5x0sli4XmC4oBzZDUA8n8vq3vWehZdf26mEQIhJuaM5pr_W42quoGyvmZjtfX2LRy-zUgOfB2SP4I6RfquMvzPbbHlDs3LwtVAdgQ"],
        ["Lasso Model", "Lasso", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/1024px-Linear_regression.svg.png"],
        ["Ridge Model", "Ridge", "https://upload.wikimedia.org/wikipedia/en/e/ed/First_order_hsked.svg"],
        ["Elastic Net Model", "ElasticNet", "https://www.researchgate.net/profile/Bart_Hobijn2/publication/46566214/figure/fig1/AS:652216872488960@1532512028126/Okuns-law-before-and-during-the-2007-recession.png"],
        ["Decision Tree Model", "DecisionTree", "https://upload.wikimedia.org/wikipedia/commons/f/ff/Decision_tree_model.png"],
        ["Random Forest Model", "RandomForest", "https://upload.wikimedia.org/wikipedia/commons/c/c7/Randomforests_ensemble.gif"],
        ["Neural Network Model", "NeuralNetwork", "https://live.staticflickr.com/8435/7880912598_389d98a505_b.jpg"]
    ]
    return jsonify(res)


@app.route("/models/plot/<modelname>/<filename>")
def plotCurves(modelname, filename):
    bytes_obj = {
        'Linear': LinearRegression.LinearRegression,
        'Lasso': Lasso.Lasso,
        'Ridge': Ridge.Ridge,
        'ElasticNet': ElasticNet.ElasticNet,
        'DecisionTree': DecisionTree.DecisionTree,
        'RandomForest': RandomForest.RandomForest,
        'NeuralNetwork': NeuralNetwork.NeuralNetwork
    }
    bo = bytes_obj.get(modelname, "Invalid model name")(path="simulator/api/trainingsets/"+filename).learning_curves()
    return send_file(bo,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/models/regression/<modelname>/<filename>")
def model_regression_results(modelname, filename):
    switcher = {
        'Linear': LinearRegression.LinearRegression,
        'Lasso': Lasso.Lasso,
        'Ridge': Ridge.Ridge,
        'ElasticNet': ElasticNet.ElasticNet,
        'DecisionTree': DecisionTree.DecisionTree,
        'RandomForest': RandomForest.RandomForest,
        'NeuralNetwork': NeuralNetwork.NeuralNetwork
    }
    global last_used_model_name
    global last_used_training_set
    last_used_model_name = modelname
    last_used_training_set = filename
    return switcher.get(modelname, "Invalid model name")(path="simulator/api/trainingsets/"+filename).regression()

@app.route("/models/predict/<modelname>/<filename>/<data_to_predict>")
def predict(modelname, filename, data_to_predict):
    switcher = {
        'Linear': LinearRegression.LinearRegression,
        'Lasso': Lasso.Lasso,
        'Ridge': Ridge.Ridge,
        'ElasticNet': ElasticNet.ElasticNet,
        'DecisionTree': DecisionTree.DecisionTree,
        'RandomForest': RandomForest.RandomForest,
        'NeuralNetwork': NeuralNetwork.NeuralNetwork
    }
    model = switcher.get(modelname, "Invalid model name")(path="simulator/api/trainingsets/"+filename)
    model.regression()
    coming_data_as_list_of_str = ast.literal_eval(data_to_predict)
    coming_data_as_list_of_floats = [float(x) for x in coming_data_as_list_of_str]
    data_to_predict_performance_for = np.array(coming_data_as_list_of_floats)
    reshaped_data = data_to_predict_performance_for.reshape(1, -1)
    print(reshaped_data)
    return str(model.predict(reshaped_data))


@app.route("/models/compare_all_models/<filename>")
def compare_all_models(filename):
    import pandas as pd
    import matplotlib.pyplot as plt

    path = "simulator/api/trainingsets/"+filename
    data = pd.read_csv(path, sep=',')
    data = data.sample(frac=1.0, random_state=0)
    y = data.iloc[:, -1:]
    X = data.iloc[:, :-1]

    y = y.to_numpy()
    X = X.to_numpy()

    # shape the data ex. (5000,)
    y = y[:, 0]

    print(X.shape)
    print(y.shape)

    Models_comparator(X, y, [("Linear", LinearRegression.LinearRegression.get_pure_model()),
                             ("Lasso", Lasso.Lasso.get_pure_model()),
                             ("Ridge", Ridge.Ridge.get_pure_model()),
                             ("ElasticNets", ElasticNet.ElasticNet.get_pure_model()),
                             ("DecisionTree", DecisionTree.DecisionTree.get_pure_model()),
                             ("RandomForest", RandomForest.RandomForest.get_pure_model()),
                             ("NeuralNetwork", NeuralNetwork.NeuralNetwork.get_pure_model())])

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    img = send_file(bytes_image,
                    attachment_filename='plot.png',
                    mimetype='image/png')
    print("The comparing img is ready to be sent")
    return img


@app.route("/models/last_training_info")
def last_training_info():
    return jsonify([last_used_model_name, last_used_training_set])


if __name__ == "__main__":
    app.run(host= '127.0.0.1', port=5001,debug=True)



