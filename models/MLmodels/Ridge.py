from MLmodels.DataReader import DataSample
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_training_result_summary
from sklearn.model_selection import ShuffleSplit
from visualizers.model_learning_curve_plotter import Learning_curve_plotter
from sklearn.linear_model import Ridge as RidgeModel
import matplotlib.pyplot as plt
import warnings


class Ridge:
    def __init__(self, data=None):
        if data is None:
            self.data = DataSample()
        else:
            self.data = data

    def regression(self):
        ridge = RidgeModel(alpha=1.0)
        ridge.fit(self.data.Xtrain, self.data.Ytrain)

        ridge_Ypred = ridge.predict(self.data.Xtest)

        ridge_mean_squared_error = mean_squared_error(self.data.Ytest, ridge_Ypred)
        ridge_r2_score = r2_score(self.data.Ytest, ridge_Ypred)

        print_training_result_summary('Ridge', ridge_mean_squared_error, ridge_r2_score)


    def plot_learning_curves(self):
        warnings.filterwarnings("ignore")
        title = "Learning Curves Ridge"
        cv = ShuffleSplit(n_splits=50, test_size=0.2, random_state=0)
        estimator = RidgeModel(alpha=0.1)
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        plt.show()

    def regression_and_plot_curves(self):
        self.regression()
        self.plot_learning_curves()

    def get_pure_model(self):
        return RidgeModel(alpha=1.0)



# Ridge().regression_and_plot_curves()