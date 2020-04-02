import pickle

from MLmodels.DataReader import DataSample
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_training_result_summary
from sklearn.model_selection import ShuffleSplit
from visualizers.model_learning_curve_plotter import Learning_curve_plotter
from sklearn.linear_model import ElasticNet as ElasticNetModel
import matplotlib.pyplot as plt
import warnings


class ElasticNet:
    def __init__(self, data=None):
        if data is None:
            self.data = DataSample()
        else:
            self.data = data

    def regression(self):
        self.eNet = ElasticNetModel(alpha=1.0)
        self.eNet.fit(self.data.Xtrain, self.data.Ytrain)

        eNet_Ypred = self.eNet.predict(self.data.Xtest)

        eNet_mean_squared_error = mean_squared_error(self.data.Ytest, eNet_Ypred)
        eNet_r2_score = r2_score(self.data.Ytest, eNet_Ypred)

        print_training_result_summary('Elastic Net', eNet_mean_squared_error, eNet_r2_score)

    def plot_learning_curves(self):
        warnings.filterwarnings("ignore")
        title = "Learning Curves ElasticNet"
        cv = ShuffleSplit(n_splits=50, test_size=0.2, random_state=0)
        estimator = ElasticNetModel(alpha=0.1)
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        plt.show()

    def regression_and_plot_curves(self):
        self.regression()
        self.plot_learning_curves()

    def get_pure_model(self):
        return ElasticNetModel(alpha=1.0)

    def save_the_trained_model(self):
        # save the model to disk
        filename = 'finalized_ElasticNet_model.sav'
        pickle.dump(self.eNet, open(filename, 'wb'))

#ElasticNet().regression_and_plot_curves()