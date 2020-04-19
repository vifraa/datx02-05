import random
import sys
sys.path.insert(0, "C:/Users/ljubo/Desktop/Repo/datx02-05/models/")
# C:\Users\ljubo\Desktop\Repo\datx02-05\models\api\flask_api.py
import os
os.chdir(os.path.dirname(__file__))
print(os.getcwd())
import pandas as pd
from IPython.display import display
from sklearn.model_selection import train_test_split
from visualizers import data_plotter

class DataSample:

    def __init__(self, path=None):
        self.read_partition(path)

    def read_partition(self, path):
        print("data reader checkpoint!")
        if path is not None:
            self.data = pd.read_csv("../data/"+ path)
            print(1111111111111111111)
        else:
            self.data = pd.read_csv("../data/regression_dataframes2.csv")
            print(22222222222222)
            # self.data = pd.read_csv("../data/regression_dataframe_medium.csv")
            # self.data = []
            # print("The data is empty")
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

        # distorting the data
        """
        rows = self.X.shape[0]
        cols = self.X.shape[1]
        for i in range(0, rows):
            for j in range(0, cols):
                self.X[i, j] = self.X[i, j] + random.randrange(0, 20)

        for i in range(0, self.Y.shape[0]):
            self.Y[i] += random.randrange(0, 20)
        """

        # testing another data set
        """ 
        from sklearn import datasets
        X, y = datasets.load_digits(return_X_y=True)
        self.Y = y
        self.X = X
        """
        # <----

        # # Partition the data into training and test sets.
        self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.X, self.Y, test_size=0.33, random_state=42)

    def data_plot_PCA(self):
        data_plotter.Reducer_plotter().pca_plot(self.Xtrain)

    def print_sample_data(self):
        print("Sample of the data: " + '\n' + "____________________")
        display(self.X.head())
        print(
            "The target (the performance of the specific person after doing the specific training): " + '\n' + "_______________________________________")
        display(self.Y.head())

