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
