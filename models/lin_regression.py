from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#Träna modellen
lr = LinearRegression()
lr.fit(Xtrain,Ytrain)

#Använd på testsettet
Ypred = lr.predict(Xtest)

print('Mean squared error: %.2f'
      % mean_squared_error(Ytest, Ypred))

# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(Ytest, Ypred))

print("Avvikelser \n",Ypred-Ytest)
#Ganska bra tbh
