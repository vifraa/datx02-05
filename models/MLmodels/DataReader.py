import pandas as pd
from IPython.display import display
from sklearn.model_selection import train_test_split
from visualizers import model_plotter

class DataSample:

    def __init__(self):
        self.read_partition()

    def read_partition(self):
        # Read the CSV file.
        self.data = pd.read_csv("../data/regression_dataframes2.csv")

        # Shuffle the dataset.
        self.data_shuffled = self.data.sample(frac=1.0, random_state=0)

        # Performance as the last column of the dataframe
        self.Y = self.data_shuffled.iloc[:, -1:]

        self.X = self.data_shuffled.iloc[:, :-1]

        # # Partition the data into training and test sets.
        self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.X, self.Y, test_size=0.2, random_state=0)

    def data_plot_PCA(self):
        model_plotter.Reducer_plotter.pca_plot(self.Xtrain)

    def print_sample_data(self):
        print("Sample of the data: " + '\n' + "____________________")
        display(self.X.head())
        print(
            "The target (the performance of the specific person after doing the specific training): " + '\n' + "_______________________________________")
        display(self.Y.head())

