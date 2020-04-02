from MLmodels.DataReader import DataSample
from MLmodels.DecisionTree import DecisionTree
from MLmodels.ElasticNets import ElasticNet
from MLmodels.Lasso import Lasso
from MLmodels.NeuralNetwork import NeuralNetwork
from MLmodels.RandomForest import RandomForest
from MLmodels.Ridge import Ridge
from visualizers.models_visual_training_comparator import Models_comparator
import warnings


class ModelsRunner:

    data = DataSample()

    models_dict = {
        'Lasso': Lasso(data), 'Ridge': Ridge(data), 'ElasticNet': ElasticNet(data),
        'DecisionTree': DecisionTree(data), 'RandomForest': RandomForest(data),
        'NeuralNetwork': NeuralNetwork(data)
    }

    def __init__(self):
        pass

    def run_models(self, model_names_list):
        for model_name in model_names_list:
            self.models_dict.get(model_name).regression()

    def run_models_and_plot_curves(self, model_names_list):
        for model_name in model_names_list:
            self.models_dict.get(model_name).regression_and_plot_curves()

    def run_all_models_and_plot_curves(self):
        for model in self.models_dict.values():
            model.regression_and_plot_curves()

    def compare_models(self, model_names_list):
        warnings.filterwarnings("ignore")
        regressors = []
        for model_name in model_names_list:
            regressor = self.models_dict.get(model_name).get_pure_model()
            regressors.append((model_name, regressor))
        Models_comparator(self.data.X, self.data.Y, regressors)

    def print_sample_data(self):
        self.data.print_sample_data()



# executing example
# ModelsRunner().run_models_and_plot_curves(['ElasticNet', 'DecisionTree'])
# MR = ModelsRunner().compare_models(['ElasticNet', 'DecisionTree', 'Lasso', 'Ridge', 'RandomForest' ])
# MR.run_all_models_and_plot_curves()
# MR.print_sample_data()




