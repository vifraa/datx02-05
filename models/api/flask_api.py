from flask import Flask, jsonify,send_file, make_response
from flask_cors import CORS, cross_origin
import sys
sys.path.insert(1, 'C:/Users/razan/Desktop/Kandidatarbetet/datx02-05/models')
import ast
import MLmodels.DecisionTree as DecisionTree
import MLmodels.ElasticNets as ElasticNet
import MLmodels.Lasso as Lasso
import MLmodels.NeuralNetwork as NeuralNetwork
import MLmodels.RandomForest as RandomForest
import MLmodels.Ridge as Ridge
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def index():
    return 'Hello from  Models!'


@app.route("/models")
def model_names():
    res = [
        ["Lasso Model", "Lasso", "https://miro.medium.com/max/4328/1*KwdVLH5e_P9h8hEzeIPnTg.png"],
        ["Ridge Model", "Ridge", "https://miro.medium.com/max/1200/1*87aMm1RRoaxS4Sy8Q-XMDg.png"],
        ["Elastic Net Model", "ElasticNet", "https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png"],
        ["Decision Tree Model", "DecisionTree", "https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png"],
        ["Random Forest Model", "RandomForest", "https://i.pinimg.com/originals/1a/dd/ef/1addef7a01f76b57aa939bd5b8ff6b57.png"],
        ["Neural Network Model", "NeuralNetwork", "https://cdn-media-1.freecodecamp.org/images/1*1mpE6fsq5LNxH31xeTWi5w.jpeg"]
    ]
    return jsonify(res)


@app.route("/models/plot/<modelname>/<filename>")
def plotCurves(modelname, filename):
    print("HERE======================================================================================================")
    bytes_obj = {
        'Lasso': Lasso.Lasso,
        'Ridge': Ridge.Ridge,
        'ElasticNet': ElasticNet.ElasticNet,
        'DecisionTree': DecisionTree.DecisionTree,
        'RandomForest': RandomForest.RandomForest,
        'NeuralNetwork': NeuralNetwork.NeuralNetwork
    }
    bo = bytes_obj.get(modelname, "Invalid model name")(path="models/api/trainingsets/"+filename).learning_curves()
    return send_file(bo,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route("/models/regression/<modelname>/<filename>")
def model_regression_results(modelname, filename):
    switcher = {
        'Lasso': Lasso.Lasso,
        'Ridge': Ridge.Ridge,
        'ElasticNet': ElasticNet.ElasticNet,
        'DecisionTree': DecisionTree.DecisionTree,
        'RandomForest': RandomForest.RandomForest,
        'NeuralNetwork': NeuralNetwork.NeuralNetwork
    }
    return switcher.get(modelname, "Invalid model name")(path="models/api/trainingsets/"+filename).regression()

@app.route("/models/predict/<modelname>/<filename>/<data_to_predict>")
def predict(modelname, filename, data_to_predict):
    switcher = {
        'Lasso': Lasso.Lasso,
        'Ridge': Ridge.Ridge,
        'ElasticNet': ElasticNet.ElasticNet,
        'DecisionTree': DecisionTree.DecisionTree,
        'RandomForest': RandomForest.RandomForest,
        'NeuralNetwork': NeuralNetwork.NeuralNetwork
    }
    model = switcher.get(modelname, "Invalid model name")(path="models/api/trainingsets/"+filename)
    model.regression()
    coming_data_as_list_of_str = ast.literal_eval(data_to_predict)
    coming_data_as_list_of_floats = [float(x) for x in coming_data_as_list_of_str]
    data_to_predict_performance_for = np.array(coming_data_as_list_of_floats)
    reshaped_data = data_to_predict_performance_for.reshape(1, -1)
    print(reshaped_data)
    return str(model.predict(reshaped_data))



if __name__ == "__main__":
    app.run(host= '127.0.0.1', port=5001,debug=True)



