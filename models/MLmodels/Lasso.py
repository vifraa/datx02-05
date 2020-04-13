import pickle
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import MLmodels.DataReader as dr
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_training_result_summary, training_result_summary
from sklearn.model_selection import ShuffleSplit, train_test_split
from visualizers.model_learning_curve_plotter import Learning_curve_plotter


class Lasso:
    """
    An object of this class can be instantiated in one of the following ways:

       * using path, ex: Lasso(path=GIVEN_PATH) then the constructor will read
            the data (csv) in the given path however its sized, just that the target is
            the located as the last column, then it partition, shuffle and instantiate the date to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using X and Y ex: Lasso(X=GIVEN_X, Y=GIVEN_Y) then the constructor will
            create data model with the given X and Y and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using already partitioned data then the constructor will
            create data model with the given data and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * if nothing of the above passed as argument ex. Lasso() then
            the constructor will read ready data using the Data_sample class
            in DataReader.py and have it in the same format specified above

    """
    def __init__(self, data=None, path=None, X=None, Y=None):
        if data is not None:
            self.data = data
        elif path is not None:
            self.read_data_from_path_and_partition(path)
        elif X is not None and Y is not None:
            self.read_X_Y_and_partition(X, Y)
        else:
            self.data = dr.DataSample()

    def read_data_from_path_and_partition(self, path):
        self.data = pd.read_csv(path)
        self.data = self.data.sample(frac=1.0, random_state=0)
        self.data.Y = self.data.iloc[:, -1:]
        self.data.X = self.data.iloc[:, :-1]
        self.data.Xtrain, self.data.Xtest, self.data.Ytrain, self.data.Ytest = train_test_split(self.data.X,
                                                                                                self.data.Y,
                                                                                                test_size=0.33,
                                                                                                random_state=42)

    def read_X_Y_and_partition(self, X, Y):
        warnings.filterwarnings("ignore")
        self.data = pd.DataFrame()
        self.data.X = X
        self.data.Y = Y
        self.data.Xtrain, self.data.Xtest, self.data.Ytrain, self.data.Ytest = train_test_split(self.data.X,
                                                                                                self.data.Y,
                                                                                                test_size=0.33,
                                                                                                random_state=42)

    def regression(self):
        self.lasso = linear_model.Lasso(alpha=0.1)
        self.lasso.fit(self.data.Xtrain, self.data.Ytrain)
        lasso_Ypred = self.lasso.predict(self.data.Xtest)

        self.lasso_mean_squared_error = mean_squared_error(self.data.Ytest, lasso_Ypred)
        self.lasso_r2_score = r2_score(self.data.Ytest, lasso_Ypred)

        print_training_result_summary('Lasso', self.lasso_mean_squared_error, self.lasso_r2_score)
        return training_result_summary('Lasso', self.lasso_mean_squared_error, self.lasso_r2_score)

    def predict(self, X_to_Predict):
        return self.lasso.predict(X_to_Predict)

    def mean_squared_error(self):
        return self.lasso_mean_squared_error

    def r2_score(self):
        return self.lasso_r2_score

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

    @classmethod
    def get_pure_model(cls):
        return linear_model.Lasso(alpha=0.1)

    def save_the_trained_model(self):
        # save the model to disk
        filename = 'finalized_Lasso_model.sav'
        pickle.dump(self.lasso, open(filename, 'wb'))

    def save_the_class_included_the_trained_model(self):
        # save the model to disk
        filename = 'class_contains_trained_Lasso_model_with_more_functionalities.sav'
        pickle.dump(self, open(filename, 'wb'))

    def get_trained_model(self):
        return self.lasso



# print(Lasso().regression())