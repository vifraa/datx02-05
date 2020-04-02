import pickle
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from MLmodels.DataReader import DataSample
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import ShuffleSplit, train_test_split
from helpers import print_training_result_summary
from visualizers.model_learning_curve_plotter import Learning_curve_plotter
from sklearn import tree



class DecisionTree:
    """
    An object of this class can be instantiated in one of the following ways:

       * using path, ex: DecisionTree(path=GIVEN_PATH) then the constructor will read
            the data in the given path, partition, shuffle and instantiate it to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using X and Y ex: DecisionTree(X=GIVEN_X, Y=GIVEN_Y) then the constructor will
            create data model with the given X and Y and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * using already partitioned data then the constructor will
            create data model with the given data and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       * if nothing of the above passed as argument ex. DecisionTree() then
            the constructor will read ready data using the Data_sample class
            in DataReader.py and have it in the same format specified above

    """
    def __init__(self, data=None, path=None, X=None, Y=None):
        if data is not None:
            self.data = data
        elif path is not None:
            self.read_data_from_path_and_partition()
        elif X is not None and Y is not None:
            self.read_X_Y_and_partition(X, Y)
        else:
            self.data = DataSample()

    def read_data_from_path_and_partition(self, path):
        self.data = pd.read_csv(path)
        self.data = self.data.sample(frac=1.0, random_state=0)
        self.data.Y = self.data['performance']
        self.data.X = self.data.drop('performance', axis=1)
        self.data.Xtrain, self.data.Xtest, self.data.Ytrain, self.data.Ytest = train_test_split(self.data.X,
                                                                                                self.data.Y,
                                                                                                test_size=0.2,
                                                                                                random_state=0)

    def read_X_Y_and_partition(self, X, Y):
        self.data.X = X
        self.data.Y = Y
        self.data.Xtrain, self.data.Xtest, self.data.Ytrain, self.data.Ytest = train_test_split(self.data.X,
                                                                                                self.data.Y,
                                                                                                test_size=0.2,
                                                                                                random_state=0)
    def regression(self):
        self.DecisionTreeM = tree.DecisionTreeRegressor()
        self.DecisionTreeM.fit(self.data.Xtrain, self.data.Ytrain)

        DecisionTree_Ypred = self.DecisionTreeM.predict(self.data.Xtest)
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

    def save_the_trained_model(self):
        # save the model to disk
        filename = 'finalized_DecisionTree_model.sav'
        pickle.dump(self.DecisionTreeM, open(filename, 'wb'))

    def save_the_class_included_the_trained_model(self):
        # save the model to disk
        filename = 'class_contains_trained_RandomForest_model_with_more_functionalities.sav'
        pickle.dump(self, open(filename, 'wb'))

#DecisionTree().regression_and_plot_curves()