import pandas as pd
from IPython.display import display
from sklearn.model_selection import train_test_split

class DataSample:

    def __init__(self):
        self.read_partition()

    def read_partition(self):
        L = []

        for i in range(90):
            L.append(f"rep{i}")
            L.append(f"weight{i}")

        L2 = ["age", "person_weight", "gender", "pre-performance", "performance"]
        L += L2

        # Read the CSV file.
        self.data = pd.read_csv("./data/regression_dataframes2.csv", names=L)

        # Shuffle the dataset.
        self.data_shuffled = self.data.sample(frac=1.0, random_state=0)

        self.Y = self.data_shuffled['performance']
        display(self.Y.head())

        # Split into input part X and output part Y.
        self.X = self.data_shuffled.drop('performance', axis=1)

        # # Partition the data into training and test sets.
        self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(self.X, self.Y, test_size=0.2, random_state=0)
