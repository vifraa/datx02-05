from MLmodels.DataReader import DataSample
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_training_result_summary
from sklearn.model_selection import ShuffleSplit
from visualizers.model_learning_curve_plotter import Learning_curve_plotter
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import warnings


class RandomForest:
    def __init__(self, data=None):
        if data is None:
            self.data = DataSample()
        else:
            self.data = data

    def regression(self):
        RandomForestM = RandomForestRegressor(max_depth=10, random_state=0)
        RandomForestM.fit(self.data.Xtrain, self.data.Ytrain)

        RandomForest_Ypred = RandomForestM.predict(self.data.Xtest)

        RandomForest_mean_squared_error = mean_squared_error(self.data.Ytest, RandomForest_Ypred)
        RandomForest_r2_score = r2_score(self.data.Ytest, RandomForest_Ypred)

        print_training_result_summary('Random Forest', RandomForest_mean_squared_error, RandomForest_r2_score)

    def plot_learning_curves(self):
        warnings.filterwarnings("ignore")
        title = "Learning Curves RandomForest"
        cv = ShuffleSplit(n_splits=50, test_size=0.2, random_state=0)
        estimator = RandomForestRegressor(max_depth=10, random_state=0)
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        plt.show()

    def regression_and_plot_curves(self):
        self.regression()
        self.plot_learning_curves()

    def get_pure_model(self):
        return RandomForestRegressor(max_depth=10, random_state=0)



# RandomForest().regression_and_plot_curves()