from mockito import when, mock, unstub
import framework.graphs as graphs
import seaborn as sns; sns.set()

responseDataSet = {
    'scatter_data': sns.load_dataset("iris"),
    'boxplot_data': sns.load_dataset("tips"),
    'barplot_data': sns.load_dataset("tips")
}


when(graphs).loadDataset('scatterplot', ...).thenReturn(responseDataSet['scatter_data'])
when(graphs).loadDataset('boxplot', ...).thenReturn(responseDataSet['scatter_data'])
when(graphs).loadDataset('barplot', ...).thenReturn(responseDataSet['scatter_data'])

when(graphs).fetchAxisInfo('barplot', ...).thenReturn(responseDataSet['scatter_data'])

