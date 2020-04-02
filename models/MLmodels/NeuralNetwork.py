import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from MLmodels.DataReader import DataSample


class NeuralNetwork:
    """
    An object of this class can be instantiated in one of the following ways:

       * using path, ex: NeuralNetwork(path=GIVEN_PATH) then the constructor will read
            the data in the given path, partition, shuffle and instantiate it to:
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
        pass

    def plot_learning_curves(self):
        pass

    def save_the_trained_model(self):
        # save the model to disk
        filename = 'finalized_Lasso_model.sav'
        pickle.dump(self.nn, open(filename, 'wb'))

    def save_the_class_included_the_trained_model(self):
        # save the model to disk
        filename = 'class_contains_trained_RandomForest_model_with_more_functionalities.sav'
        pickle.dump(self, open(filename, 'wb'))
