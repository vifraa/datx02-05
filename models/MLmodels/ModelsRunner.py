import pandas as pd
import sys
sys.path.insert(0, "C:/Users/ljubo/Desktop/Repo/datx02-05/models/")
import MLmodels.DataReader as dr
from MLmodels.DecisionTree import DecisionTree
from MLmodels.ElasticNets import ElasticNet
from MLmodels.Lasso import Lasso
from MLmodels.NeuralNetwork import NeuralNetwork
from MLmodels.RandomForest import RandomForest
from MLmodels.Ridge import Ridge
from visualizers import data_plotter
from visualizers.models_visual_training_comparator import Models_comparator
import warnings
from json import dumps

class ModelsRunner:
    """
    models_dict = {
        'Lasso': Lasso(),
        'Ridge': Ridge(),
        'ElasticNet': ElasticNet(),
        'DecisionTree': DecisionTree(),
        'RandomForest': RandomForest(),
        'NeuralNetwork': NeuralNetwork()
    }
    """
    def __init__(self, path=None):
        pass
        """
        if path is not None:
            self.data = dr.DataSample(path)
        else:
            self.data = dr.DataSample()
        """

    def train_all_models(self):
        for model in self.models_dict.values():
            model.regression()

    def train_specific_models(self, model_names_list):
        for model_name in model_names_list:
            self.models_dict.get(model_name).regression()

    def train_specific_models_and_plot_curves(self, model_names_list):
        for model_name in model_names_list:
            self.models_dict.get(model_name).regression_and_plot_curves()

    def train_all_models_and_plot_curves(self):
        for model in self.models_dict.values():
            model.regression_and_plot_curves()

    def get_instance_of_model(self, model_name):
        self.models_dict.get(model_name)

    def compare_models(self, model_names_list):
        warnings.filterwarnings("ignore")
        regressors = []
        for model_name in model_names_list:
            regressor = self.models_dict.get(model_name).get_pure_model()
            regressors.append((model_name, regressor))
        Models_comparator(self.data.X, self.data.Y, regressors)

    def print_sample_data(self):
        self.data.print_sample_data()

    def plot_sample_data_pca(self):
        self.data.data_plot_PCA()

    def train_all_models_on_specific_data_and_then_save_them_all_as_binary_sav_files(self, X, Y):
        trained_models = [Lasso(X=X, Y=Y), Ridge(X=X, Y=Y), ElasticNet(X=X, Y=Y),
                          DecisionTree(X=X, Y=Y), RandomForest(X=X, Y=Y), NeuralNetwork(X=X, Y=Y)]
        for model in trained_models:
            model.regression()
            model.save_the_class_included_the_trained_model()


    def train_all_models_on_specific_data_using_path(self, path):
        trained_models = [Lasso(path=path), Ridge(path=path), ElasticNet(path=path),
                          DecisionTree(path=path), RandomForest(path=path), NeuralNetwork(path=path)]
        for model in trained_models:
            model.regression_and_plot_curves()


    def train_specific_models_on_specific_data_and_then_save_them_all_as_binary_sav_files_with_path(self, path, model_name):
        switcher = {
            'Lasso': Lasso(path=path).save_the_class_included_the_trained_model(),
            'Ridge': Ridge(path=path).save_the_class_included_the_trained_model(),
            'ElasticNet': ElasticNet(path=path).save_the_class_included_the_trained_model(),
            'DecisionTree': DecisionTree(path=path).save_the_class_included_the_trained_model(),
            'RandomForest': RandomForest(path=path).save_the_class_included_the_trained_model(),
            'NeuralNetwork': NeuralNetwork(path=path).save_the_class_included_the_trained_model()
        }
        switcher.get(model_name, "Invalid model name")


# executing example
# ModelsRunner().train_specific_models_and_plot_curves(['ElasticNet', 'DecisionTree'])
# ModelsRunner().compare_models(['ElasticNet', 'DecisionTree', 'Lasso', 'Ridge', 'RandomForest' ])
# ModelsRunner().train_all_models_and_plot_curves()
# MR.print_sample_data()
# ModelsRunner().train_all_models()
# Lasso(X=DataSample().X, Y=DataSample().Y).regression()
# ModelsRunner().train_all_models_on_specific_data_and_then_save_them_all_as_binary_sav_files(DataSample().X, DataSample().Y)
# filename = 'class_contains_trained_NeuralNetwork_model_with_more_functionalities.sav'
# loaded_model = pickle.load(open(filename, 'rb'))
# print(loaded_model.r2_score())


# MR = ModelsRunner()
# MR.train_all_models_and_plot_curves()


#df = pd.read_csv('../data/regression_dataframe_medium.csv', sep=',')
#df.applymap(test_str)
#df.to_csv('../data/str_regression_dataframe_medium.csv', index=False)

#from sklearn import datasets
#X, y = datasets.load_digits(return_X_y=True)

MR = ModelsRunner(path="../data/6w_pb_fiesta_3000_pop/program_logs.csv")
MR.train_all_models_on_specific_data_using_path(path="../data/6w_pb_fiesta_3000_pop/program_logs.csv")
