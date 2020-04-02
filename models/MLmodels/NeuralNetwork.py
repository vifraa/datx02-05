import pickle

from MLmodels.DataReader import DataSample


class NeuralNetwork:
    def __init__(self, data=None):
        if data is None:
            self.data = DataSample()
        else:
            self.data = data
        self.regression()

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
