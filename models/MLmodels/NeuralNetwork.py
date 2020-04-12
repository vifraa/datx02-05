import pickle
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, ShuffleSplit
from MLmodels.DataReader import DataSample
from sklearn.neural_network import MLPRegressor
from helpers import print_training_result_summary, training_result_summary
from visualizers.model_learning_curve_plotter import Learning_curve_plotter


class NeuralNetwork:
    """
    An object of this class can be instantiated in one of the following ways:

       * using path, ex: NeuralNetwork(path=GIVEN_PATH) then the constructor will read
            the data (csv) in the given path however its sized, just that the target is
            the located as the last column, then it partition, shuffle and instantiate the date to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using X and Y ex: NeuralNetwork(X=GIVEN_X, Y=GIVEN_Y) then the constructor will
            create data model with the given X and Y and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using already partitioned data then the constructor will
            create data model with the given data and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * if nothing of the above passed as argument ex. NeuralNetwork() then
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

    @classmethod
    def get_pure_model(cls):
        return MLPRegressor(
                            hidden_layer_sizes=(100, 100),
                            activation='relu',
                            solver='adam',
                            alpha=0.0001,
                            batch_size='auto',
                            learning_rate='constant',
                            learning_rate_init=0.001,
                            power_t=0.5,
                            max_iter=10000,
                            shuffle=True,
                            random_state=None,
                            tol=0.0001,
                            verbose=False,
                            warm_start=False,
                            momentum=0.9,
                            nesterovs_momentum=True,
                            early_stopping=True,
                            validation_fraction=0.1,
                            beta_1=0.9,
                            beta_2=0.999,
                            epsilon=1e-08,
                            n_iter_no_change=100,
                            max_fun=15000
                        )

    def regression(self):
        self.nn = self.get_pure_model()
        self.nn.fit(self.data.Xtrain, np.asarray(self.data.Ytrain).flatten())
        nn_Ypred = self.nn.predict(self.data.Xtest)
        self.nn_mean_squared_error = mean_squared_error(self.data.Ytest, nn_Ypred)
        self.nn_r2_score = r2_score(self.data.Ytest, nn_Ypred)
        print_training_result_summary('NeuralNetwork', self.nn_mean_squared_error, self.nn_r2_score)
        return training_result_summary('NeuralNetwork', self.nn_mean_squared_error, self.nn_r2_score)

    def predict(self, X_to_Predict):
        return self.nn.predict(X_to_Predict)

    def mean_squared_error(self):
        return self.nn_mean_squared_error

    def r2_score(self):
        return self.nn_r2_score

    def plot_learning_curves(self):
        warnings.filterwarnings("ignore")
        title = "Learning Curves NeuralNetwork"
        cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
        estimator = self.get_pure_model()
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        plt.show()

    def regression_and_plot_curves(self):
        self.regression()
        self.plot_learning_curves()

    def save_the_trained_model(self):
        # save the model to disk
        filename = 'finalized_Lasso_model.sav'
        pickle.dump(self.nn, open(filename, 'wb'))

    def save_the_class_included_the_trained_model(self):
        # save the model to disk
        filename = 'class_contains_trained_NeuralNetwork_model_with_more_functionalities.sav'
        pickle.dump(self, open(filename, 'wb'))

    def get_trained_model(self):
        return self.nn



# NeuralNetwork().regression_and_plot_curves()


