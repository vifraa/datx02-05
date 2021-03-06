import random

import pandas as pd
from IPython.display import display
from sklearn.model_selection import train_test_split
#from visualizers import data_plotter

class DataSampleValues:

    def __init__(self, x, y):
        self.X = x
        self.Y = y

        self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.X, self.Y, test_size=0.33, random_state=42)


class DataSample:

    def __init__(self, path=None):
        self.read_partition(path)

    def read_partition(self, path):
        if path is not None:
            self.data = pd.read_csv(path)
        else:
             self.data = pd.read_csv("../regression_dataframes2.csv")

        # Shuffle the dataset.
        self.data_shuffled = self.data.sample(frac=1.0, random_state=0)

        # Performance as the last column of the dataframe
        self.Y = self.data_shuffled.iloc[:, -1:]
        self.X = self.data_shuffled.iloc[:, :-1]

        # debugging code ---->
        # converting the data to numpy arrays
        self.Y = self.Y.to_numpy()
        self.X = self.X.to_numpy()

        # shape the data ex. (5000,)
        self.Y = self.Y[:, 0]

        # Partition the data into training and test sets.
        self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.X, self.Y, test_size=0.33, random_state=42)

    def data_plot_PCA(self):
        data_plotter.Reducer_plotter().pca_plot(self.Xtrain)

    def print_sample_data(self):
        print("Sample of the data: " + '\n' + "____________________")
        display(self.X.head())
        print(
            "The target (the performance of the specific person after doing the specific training): " + '\n' + "_______________________________________")
        display(self.Y.head())


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("../api/trainingsets/ttrtest.csv", sep=',')
data = data.head(100)
data.plot()
plt.show()