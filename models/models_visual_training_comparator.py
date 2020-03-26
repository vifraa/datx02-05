import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron


class Compare:

    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.compare_models()

    def compare_models(self):
        heldout = [0.95, 0.90, 0.75, 0.50, 0.01]
        rounds = 20

        regressors = [
            ("Perceptron", Perceptron())
        ]

        xx = 1. - np.array(heldout)

        for name, clf in regressors:
            print("training %s" % name)
            rng = np.random.RandomState(42)
            yy = []
            for i in heldout:
                yy_ = []
                for r in range(rounds):
                    X_train, X_test, y_train, y_test = \
                        train_test_split(self.X, self.y, test_size=i, random_state=rng)
                    clf.fit(X_train, y_train)
                    y_pred = clf.predict(X_test)
                    yy_.append(1 - np.mean(y_pred == y_test))
                yy.append(np.mean(yy_))
            plt.plot(xx, yy, label=name)

        plt.legend(loc="upper right")
        plt.xlabel("Proportion train")
        plt.ylabel("Test Error Rate")
        plt.show()


'''
testing learning perceptrons on digit data set
'''
from sklearn import datasets
X, y = datasets.load_digits(return_X_y=True)
Compare(X, y)