from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from MLmodels.DecisionTree import DecisionTree
from MLmodels.ElasticNets import ElasticNet
import MLmodels.Lasso as Lasso
from MLmodels.NeuralNetwork import NeuralNetwork
from MLmodels.RandomForest import RandomForest
from MLmodels.Ridge import Ridge

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    return 'Hello world!'


@app.route("/models")
def model_names():
    res = {
        "Lasso Model": "https://miro.medium.com/max/4328/1*KwdVLH5e_P9h8hEzeIPnTg.png",
        "Ridge Model": "https://miro.medium.com/max/1200/1*87aMm1RRoaxS4Sy8Q-XMDg.png",
        "Elastic Net Model": "https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png",
        "Decision Tree Model": "https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png",
        "Random Forest Model": "https://i.pinimg.com/originals/1a/dd/ef/1addef7a01f76b57aa939bd5b8ff6b57.png",
        "Neural Network Model": "https://cdn-media-1.freecodecamp.org/images/1*1mpE6fsq5LNxH31xeTWi5w.jpeg"
    }
    return jsonify(res)


@app.route("/models/regression/<modelname>")
def model_regression_results(modelname):

     switcher = {
        'Lasso': Lasso().regression(),
        'Ridge': Ridge().regression(),
        'ElasticNet': ElasticNet().regression(),
        'DecisionTree': DecisionTree().regression(),
        'RandomForest': RandomForest().regression(),
        'NeuralNetwork': NeuralNetwork().regression()
    }

    #return modelname
    # return switcher.get(modelname, "Invalid model name")


if __name__ == "__main__":
    app.run(debug=True)
