from MLmodels.DataReader import DataSample
from MLmodels.DecisionTree import DecisionTree
from MLmodels.ElasticNets import ElasticNet
from MLmodels.Lasso import Lasso
from MLmodels.NeuralNetwork import NeuralNetwork
from MLmodels.RandomForest import RandomForest
from MLmodels.Ridge import Ridge


class ModelsRunner:
    data = DataSample()
    models_dict = {'Lasso': Lasso(data), 'Ridge': Ridge(data), 'ElasticNet': ElasticNet(data),
                   'DecisionTree': DecisionTree(data), 'RandomForest': RandomForest(data),
                   'NeuralNetwork': NeuralNetwork(data)}

    def __init__(self):
        pass

    def run_models (self, model_names_list):
        for model_name in model_names_list:
            self.models_dict.get(model_name).regression()

    def run_models_and_plot_curves(self, model_names_list):
        for model_name in model_names_list:
            self.models_dict.get(model_name).regression_and_plot_curves()

    def run_all_models_and_plot_curves(self):
        for model in self.models_dict.values():
            model.regression_and_plot_curves()


# executing example
# ModelsRunner().run_models_and_plot_curves(['ElasticNet', 'DecisionTree'])

