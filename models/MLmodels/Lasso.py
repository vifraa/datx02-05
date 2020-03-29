from MLmodels.DataReader import DataSample
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_training_result_summary
from sklearn.model_selection import ShuffleSplit
import matplotlib.pyplot as plt
from visualizers.model_learning_curve_plotter import Learning_curve_plotter
import warnings


class Lasso:
    def __init__(self, data=None):
        if data is None:
            self.data = DataSample()
        else:
            self.data = data

    def regression(self):
        lasso = linear_model.Lasso(alpha=0.1)
        lasso.fit(self.data.Xtrain, self.data.Ytrain)
        lasso_Ypred = lasso.predict(self.data.Xtest)

        lasso_mean_squared_error = mean_squared_error(self.data.Ytest, lasso_Ypred)
        lasso_r2_score = r2_score(self.data.Ytest, lasso_Ypred)

        print_training_result_summary('Lasso', lasso_mean_squared_error, lasso_r2_score)

    def plot_learning_curves(self):
        warnings.filterwarnings("ignore")
        title = "Learning Curves Lasso"
        cv = ShuffleSplit(n_splits=50, test_size=0.2, random_state=0)
        estimator = linear_model.Lasso(alpha=0.1)
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        plt.show()

    def regression_and_plot_curves(self):
        self.regression()
        self.plot_learning_curves()

    def get_pure_model(self):
        return linear_model.Lasso(alpha=0.1)

#Lasso().regression_and_plot_curves()