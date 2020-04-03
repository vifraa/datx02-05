# Machine Learning Models & Visualizers

## Machine Learning Models

#### We provide 6 Machine Learning models to do the regression:

- Lasso
- Ridge
- Elastic Net
- Decision Tree
- Random Forest
- Neural Network (fully connected perceptrons)

#### Using the models:
You can use the models using ModelsRunner class or by using the specific model directly.

#### Using the models by ModelsRunner:
ModelsRunner has the following interface:

 ```
    def train_all_models():

    def train_specific_models(model_names_list):

    train_specific_models_and_plot_curves(model_names_list)

    train_all_models_and_plot_curves()

    get_instance_of_model(model_name)

    compare_models(model_names_list)

    print_sample_data()

    train_all_models_on_specific_data_and_then_save_them_all_as_binary_sav_files(X, Y):

```

#### using a specific model directly:
All the models have the same following interface:

An object of the class of the model can be instantiated in one of the following ways:

       - using path, ex: DecisionTree(path=GIVEN_PATH) then the constructor will read
            the data (csv) in the given path however its sized, just that the target is
            the located as the last column, then it partition, shuffle and instantiate the date to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       - using X and Y ex: DecisionTree(X=GIVEN_X, Y=GIVEN_Y) then the constructor will
            create data model with the given X and Y and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       - using already partitioned data then the constructor will
            create data model with the given data and partition it also to:
            self.data.Xtrain, self.data.Ytrain, self.data.Xtest, self.data.Ytest

       - if nothing of the above passed as argument ex. DecisionTree() then
            the constructor will read ready data using the Data_sample class
            in DataReader.py and have it in the same format specified above

```
    def read_data_from_path_and_partition(path):

    def read_X_Y_and_partition(X, Y):

    def regression() # does the regression

    def predict(X_to_Predict)

    def mean_squared_error()

    def r2_score()

    def plot_learning_curves()

    def regression_and_plot_curves()

    @classmethod
    def get_pure_model)

    def save_the_trained_model()
        # save just the trined model to disk

    def save_the_class_included_the_trained_model()
        # save the class included the trained model to disk as a binary sav file

    get_trained_model(self)

```


## Visualizers
- Learning curves plotter: Plots the score of the model on the training set versus the validation set, plots the scalability of the model and the performance of the model.
- Validation curves plotter: plots the Validation curves of the models
- Data plotter: Reduces the dimensionality of the data using principal component analysis and plot it on a 2D plane, that helps observing eventual correlations in the data. 
- Models comparator: Plots test error curves of all the models to compare them 

# The easiest way to use the model 
 - train all the models on your data (do the regression) and save all the trained models into sav files which you can use easily when you want. The good news that ModelsRunner does all of that for you with just one command: 
```
ModelsRunner().train_all_models_on_specific_data_and_then_save_them_all_as_binary_sav_files(YOURDATA_X, YOURDATA_Y)
```
Then you see in the same directory 6 sav files which has the classes of the models, each includes the trained model and more functionalitis that the interface above descibes.

## Example working with the models:
Here we take an example on how simply to use the trained and saved NeuralNetwork model:

```
filename = 'class_contains_trained_NeuralNetwork_model_with_more_functionalities.sav'
loaded_model = pickle.load(open(filename, 'rb'))
loaded_model.predict(YOURDATA_X) # to use the model in prediction
```
You can also easily use other interesting methods that the model class provids, for example:

```
loaded_model.mean_squared_error() # to see the mean squared error of the model
loaded_model.r2_score() # to see the r2 score of the model
loaded_model.plot_learning_curves() # to plot the 3 learning curves of the model
loaded_model.get_trained_model() # if you want to do more direct operations on the trained model
```
