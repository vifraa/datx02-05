from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# can be tested directly in 90-sets-model
class Reducer_plotter:

    def __init__(self):
        pass
    def pca_plot(self, dff):
        df = pd.DataFrame(dff)
        pca = PCA(n_components=3)
        Xtest_plot = df.copy()
        pca_result = pca.fit_transform(Xtest_plot.values)
        Xtest_plot['pca-one'] = pca_result[:, 0]
        Xtest_plot['pca-two'] = pca_result[:, 1]
        Xtest_plot['pca-three'] = pca_result[:, 2]

        print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

        plt.figure(figsize=(16, 10))
        sns.scatterplot(
            x="pca-one", y="pca-two",
            data=Xtest_plot.loc[:, :]
        )

        '''
        sns.scatterplot(
            x="pca-one", y="pca-two",
            hue="Ytest",
            palette=sns.color_palette("hls", 10),
            data=Xtest_plot.loc[:,:],
            legend="full",
            alpha=0.3
        )
        '''


