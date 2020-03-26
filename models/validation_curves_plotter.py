import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import validation_curve

class validation_curve_plot:
    def __init__(self, X, y, estimator, param_name):
        self.X = X
        self.y = y
        self.estimator = estimator
        self.param_name = param_name
        self.validate()

    def validate(self):
        param_range = np.logspace(-6, -1, 5)
        train_scores, test_scores = validation_curve(
            self.estimator, self.X, self.y, param_name=self.param_name, param_range=param_range,
            scoring="accuracy", n_jobs=1)
        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)

        plt.title("Validation Curve with SVM")
        plt.xlabel(r"$\gamma$")
        plt.ylabel("Score")
        plt.ylim(0.0, 1.1)
        lw = 2
        plt.semilogx(param_range, train_scores_mean, label="Training score",
                     color="darkorange", lw=lw)
        plt.fill_between(param_range, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.2,
                         color="darkorange", lw=lw)
        plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
                     color="navy", lw=lw)
        plt.fill_between(param_range, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.2,
                         color="navy", lw=lw)
        plt.legend(loc="best")
        plt.show()



'''
testing learning perceptrons and SVC on digit data set
'''
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron
X, y = datasets.load_digits(return_X_y=True)
validation_curve_plot(X, y, Perceptron(), "alpha")
validation_curve_plot(X, y, SVC(), "gamma")
