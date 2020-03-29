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

    def __init__(self, model_names_list):
        pass #self.run_models_and_plot_curves()

    def run_all_models_and_plot_curves(self):
        for model in self.models_dict.values():
            model.plot_learning_curves()



ModelsRunner([]).run_all_models_and_plot_curves()