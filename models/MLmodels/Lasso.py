from MLmodels.DataReader import DataSample
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from helpers import print_mean_squared_error, print_coefficient_of_determination

class Lasso:
    def __init__(self, data=None):
        if data is None:
            self.data = DataSample()
        else:
            self.data = data
        self.regression()

    def regression(self):
        lasso = linear_model.Lasso(alpha=0.1)
        lasso.fit(self.data.Xtrain, self.data.Ytrain)
        lasso_Ypred = lasso.predict(self.data.Xtest)

        lasso_mean_squared_error = mean_squared_error(self.data.Ytest, lasso_Ypred)
        lasso_r2_score = r2_score(self.data.Ytest, lasso_Ypred)

        print_mean_squared_error(lasso_mean_squared_error)
        print_coefficient_of_determination(lasso_r2_score)

        
