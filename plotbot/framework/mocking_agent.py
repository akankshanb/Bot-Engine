from mockito import when, mock, unstub
import graphs

when(graphs).loadDataset('scatterplot', ...).thenReturn(response['scatter_data'])
when(graphs).loadDataset('boxplot', ...).thenReturn(response['scatter_data'])
when(graphs).loadDataset('barplot', ...).thenReturn(response['scatter_data'])

