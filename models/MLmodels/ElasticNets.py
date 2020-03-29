from MLmodels.DataReader import DataSample
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_mean_squared_error, print_coefficient_of_determination
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
        self.regression()

    def regression(self):
        eNet = ElasticNetModel(alpha=1.0)
        eNet.fit(self.data.Xtrain, self.data.Ytrain)

        eNet_Ypred = eNet.predict(self.data.Xtest)

        eNet_mean_squared_error = mean_squared_error(self.data.Ytest, eNet_Ypred)
        eNet_r2_score = r2_score(self.data.Ytest, eNet_Ypred)

        print_mean_squared_error(eNet_mean_squared_error)
        print_coefficient_of_determination(eNet_r2_score)
