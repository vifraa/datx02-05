import pickle
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from MLmodels.DataReader import DataSample
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_training_result_summary, training_result_summary
from sklearn.model_selection import ShuffleSplit, train_test_split
from visualizers.model_learning_curve_plotter import Learning_curve_plotter
from sklearn.linear_model import Ridge as RidgeModel



class Ridge:
    """
    An object of this class can be instantiated in one of the following ways:

       * using path, ex: Ridge(path=GIVEN_PATH) then the constructor will read
            the data (csv) in the given path however its sized, just that the target is
            the located as the last column, then it partition, shuffle and instantiate the date to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using X and Y ex: Ridge(X=GIVEN_X, Y=GIVEN_Y) then the constructor will
            create data model with the given X and Y and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using already partitioned data then the constructor will
            create data model with the given data and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * if nothing of the above passed as argument ex. Ridge() then
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
            self.data = DataSample()

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
        self.data = pd.DataFrame()
        self.data.X = X
        self.data.Y = Y
        self.data.Xtrain, self.data.Xtest, self.data.Ytrain, self.data.Ytest = train_test_split(self.data.X,
                                                                                                self.data.Y,
                                                                                                test_size=0.33,
                                                                                                random_state=42)

    def regression(self):
        self.ridge = RidgeModel(alpha=1.0)
        self.ridge.fit(self.data.Xtrain, self.data.Ytrain)

        ridge_Ypred = self.ridge.predict(self.data.Xtest)

        self.ridge_mean_squared_error = mean_squared_error(self.data.Ytest, ridge_Ypred)
        self.ridge_r2_score = r2_score(self.data.Ytest, ridge_Ypred)

        print_training_result_summary('Ridge', self.ridge_mean_squared_error, self.ridge_r2_score)
        return training_result_summary('Ridge', self.ridge_mean_squared_error, self.ridge_r2_score)

    def predict(self, X_to_Predict):
        return self.ridge.predict(X_to_Predict)

    def mean_squared_error(self):
        return self.ridge_mean_squared_error

    def r2_score(self):
        return self.ridge_r2_score

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

    @classmethod
    def get_pure_model(cls):
        return RidgeModel(alpha=1.0)

    def save_the_trained_model(self):
        # save the model to disk
        filename = 'finalized_Ridge_model.sav'
        pickle.dump(self.ridge, open(filename, 'wb'))

    def save_the_class_included_the_trained_model(self):
        # save the model to disk
        filename = 'class_contains_trained_Ridge_model_with_more_functionalities.sav'
        pickle.dump(self, open(filename, 'wb'))

    def get_trained_model(self):
        return self.ridge



# Ridge().regression_and_plot_curves()