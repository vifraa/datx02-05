import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron


class Models_comparator:

    def __init__(self, X, y, regressors):
        self.X = X
        self.y = y
        self.regressors = regressors
        self.compare_models()

    def compare_models(self):
        heldout = [0.95, 0.90, 0.75, 0.50, 0.01]
        rounds = 20

        xx = 1. - np.array(heldout)

        for name, clf in self.regressors:
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
testing learning perceptrons and stochastic gradient decent on digit data set
'''

def comparator_test():
    from sklearn import datasets
    from sklearn.linear_model import SGDClassifier, Perceptron
    X, y = datasets.load_digits(return_X_y=True)
    regressors = [("SGD", SGDClassifier(max_iter=100)), ("Perceptron", Perceptron())]
    Models_comparator(X, y, regressors)

comparator_test()