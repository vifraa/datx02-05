import pandas as pd
from sklearn.model_selection import train_test_split

L = []
data.shape
for i in range(90):
    L.append(f"rep{i}")
    L.append(f"weight{i}")

L2 = ["age", "person_weight", "gender", "performance"]
L += L2

# Read the CSV file.
data = pd.read_csv("regression_dataframes.csv", names=L)

# Shuffle the dataset.
data_shuffled = data.sample(frac=1.0, random_state=0)

# Split into input part X and output part Y.
X = data_shuffled.drop('performance', axis=1)
X.head()
Y = data_shuffled['performance']
Y.head()

# # Partition the data into training and test sets.
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2, random_state=0)