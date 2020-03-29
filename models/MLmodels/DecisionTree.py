from MLmodels.DataReader import DataSample
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import ShuffleSplit
from helpers import print_training_result_summary
from visualizers.model_learning_curve_plotter import Learning_curve_plotter
from sklearn import tree
import matplotlib.pyplot as plt
import warnings


class DecisionTree:
    def __init__(self, data=None):
        if data is None:
            self.data = DataSample()
        else:
            self.data = data

    def regression(self):
        DecisionTreeM = tree.DecisionTreeRegressor()
        DecisionTreeM.fit(self.data.Xtrain, self.data.Ytrain)

        DecisionTree_Ypred = DecisionTreeM.predict(self.data.Xtest)

        DecisionTree_mean_squared_error = mean_squared_error(self.data.Ytest, DecisionTree_Ypred)
        DecisionTree_r2_score = r2_score(self.data.Ytest, DecisionTree_Ypred)

        print_training_result_summary('Decision Tree', DecisionTree_mean_squared_error, DecisionTree_r2_score)

    def plot_learning_curves(self):
        warnings.filterwarnings("ignore")
        title = "Learning Curves DecisionTree"
        cv = ShuffleSplit(n_splits=50, test_size=0.2, random_state=0)
        estimator = tree.DecisionTreeRegressor()
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        plt.show()

    def regression_and_plot_curves(self):
        self.regression()
        self.plot_learning_curves()

    def get_pure_model(self):
        return tree.DecisionTreeRegressor()



#DecisionTree().regression_and_plot_curves()