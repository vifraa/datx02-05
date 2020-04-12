from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello world!'


@app.route("/models", methods=["GET"])
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


if __name__ == "__main__":
    app.run(debug=True)
