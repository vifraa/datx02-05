import pickle
import pandas as pd
import warnings
import io
import matplotlib.pyplot as plt
#import MLmodels.DataReader as dr
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_training_result_summary, training_result_summary
from sklearn.model_selection import ShuffleSplit, train_test_split
from visualizers.model_learning_curve_plotter import Learning_curve_plotter



class LinearRegression:
    """
    A wrapper class for a sklearn Linear Regression machine learning model.
    """
    def __init__(self, data=None, path=None, X=None, Y=None):
        if data is not None:
            self.data = data
        elif path is not None:
            self.read_data_from_path_and_partition(path)
        elif X is not None and Y is not None:
            self.read_X_Y_and_partition(X, Y)
        #else:
        #    self.data = dr.DataSample()


    def read_data_from_path_and_partition(self, path):
        self.data = pd.read_csv(path)
        self.data = self.data.sample(frac=1.0, random_state=0)
        self.data.Y = self.data.iloc[:, -1:]
        self.data.X = self.data.iloc[:, :-1]
        self.data.Xtrain, self.data.Xtest, self.data.Ytrain, self.data.Ytest = train_test_split(
            self.data.X, self.data.Y, test_size=0.33, random_state=42)

    def read_X_Y_and_partition(self, X, Y):
        warnings.filterwarnings("ignore")
        self.data = pd.DataFrame()
        self.data.X = X
        self.data.Y = Y
        self.data.Xtrain, self.data.Xtest, self.data.Ytrain, self.data.Ytest = train_test_split(
            self.data.X, self.data.Y, test_size=0.33, random_state=42)

    def regression(self):
        """
        Traing the machine learning model on the internal data.
        """
        self.model = linear_model.LinearRegression()
        self.model.fit(self.data.Xtrain, self.data.Ytrain)
        model_Ypred = self.model.predict(self.data.Xtest)

        self.model_mean_squared_error = mean_squared_error(self.data.Ytest, model_Ypred)
        self.model_r2_score = r2_score(self.data.Ytest, model_Ypred)

        print_training_result_summary(
            'LinearRegression', self.model_mean_squared_error, self.model_r2_score)

        self.save_the_trained_model()
        self.save_the_class_included_the_trained_model()
        return training_result_summary(
            'LinearRegression', self.model_mean_squared_error, self.model_r2_score)

    def predict(self, X_to_Predict):
        """
        Predicts based on input.
        """
        return self.model.predict(X_to_Predict)

    def mean_squared_error(self):
        """
        Returns the models mean squared error.
        """
        return self.model_mean_squared_error

    def r2_score(self):
        """
        Returns the models r2_score.
        """
        return self.model_r2_score

    def plot_learning_curves(self):
        """
        Plots the learning curves of the model..
        """
        warnings.filterwarnings("ignore")
        title = "Learning Curves LinearRegression"
        cv = ShuffleSplit(n_splits=50, test_size=0.2, random_state=0)
        estimator = linear_model.LinearRegression()
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        plt.show()

    def learning_curves(self):
        warnings.filterwarnings("ignore")
        title = "Learning Curves LinearRegression"
        cv = ShuffleSplit(n_splits=50, test_size=0.2, random_state=0)
        estimator = linear_model.LinearRegression()
        Learning_curve_plotter(estimator, title, self.data.X, self.data.Y, cv=cv)
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image

    def regression_and_plot_curves(self):
        """
        Learn based on the internal data and plots the learning curves 
        """
        self.regression()
        self.plot_learning_curves()

    @classmethod
    def get_pure_model(cls):
        """
        Returns a new, untrained, version of the machine learning model.
        """
        return linear_model.LinearRegression()

    def save_the_trained_model(self):
        # save the model to disk
        filename = 'finalized_Linear_model.sav'
        pickle.dump(self.model, open('simulator/api/'+filename, 'wb'))

    def save_the_class_included_the_trained_model(self):
        # save the model to disk
        filename = 'class_contains_trained_Linear_model_with_more_functionalities.sav'
        pickle.dump(self, open('simulator/api/'+filename, 'wb'))

    def train_and_save_the_class_included_the_trained_model(self, dataset_name):
        self.regression_and_plot_curves()
        # save the model to disk
        filename = 'class_contains_trained_Linear_model_on_' + dataset_name + '_with_more_functionalities.sav'
        pickle.dump(self, open('simulator/api/'+filename, 'wb'))

    def get_trained_model(self):
        """
        Returns the trained machine learning model.
        """
        return self.model
