from mockito import when, mock, unstub
import framework.graphs as graphs
import service.sampler as sampler
import framework.mixin as mixin
import service.retrieval as retrieval
import seaborn as sns; sns.set()
from random import randint
import subprocess
import re
import framework.constants as constants

responseDataSet = {
    'scatter_data': sns.load_dataset("iris"),
    'boxplot_data': sns.load_dataset("tips"),
    'barplot_data': sns.load_dataset("tips")
}
scatter_axis = {
        'x-axis':   responseDataSet['scatter_data'].sepal_length,
        'y-axis':   responseDataSet['scatter_data'].sepal_width
    }
boxplot_axis = {
        'x-axis':   "day",
        'y-axis':   "total_bill",
    }
barplot_axis= {
        'x-axis':  "tip",
        'y-axis':  "day"
    }
responseAxisInfo = {
    'scatter_axis': scatter_axis,
    'boxplot_axis': boxplot_axis,
    'barplot_axis': barplot_axis
}
responseRetrieve = {}

responseSnippet={
    "scatterplot": ["scatterplot_code","scatterplot_graph"],
    "barplot": ["barplot_code","barplot_graph"], 
    "boxplot": ["boxplot_code","boxplot_graph"]
}

def generateScatterMockPlot():
    axis_info = graphs.fetchAxisInfo('scatterplot', '')
    dataset = graphs.load_dataset('scatterplot', '')
    newGraph = graphs.scatter_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage()
    return newGraph.plotLocation

def generateBarMockPlot():
    axis_info = graphs.fetchAxisInfo('barplot', '')
    dataset = graphs.load_dataset('barplot', '')
    newGraph = graphs.bar_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage()
    return newGraph.plotLocation

def generateBoxMockPlot():
    axis_info = graphs.fetchAxisInfo('boxplot', '')
    dataset = graphs.load_dataset('boxplot', '')
    newGraph = graphs.box_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage()
    return newGraph.plotLocation

def generateMockPlots():
    numScatter, numBar, numBox = randint(0,10), randint(0,10), randint(0,10)
    plots = []
    for i in range(0, numScatter):
        plots.append(generateScatterMockPlot())
    for i in range(0,numBar):
        plots.append(generateBarMockPlot())
    for i in range(0,numBox):
        plots.append(generateBoxMockPlot())
    print("Mock data generation complete...")
    return plots

when(mixin).fetchDB_path().thenReturn('framework/allplots/')
when(graphs).load_dataset('scatterplot', ...).thenReturn(responseDataSet['scatter_data'])
when(graphs).load_dataset('boxplot', ...).thenReturn(responseDataSet['boxplot_data'])
when(graphs).load_dataset('barplot', ...).thenReturn(responseDataSet['barplot_data'])

when(graphs).fetchAxisInfo('scatterplot', ...).thenReturn(responseAxisInfo['scatter_axis'])
when(graphs).fetchAxisInfo('boxplot', ...).thenReturn(responseAxisInfo['boxplot_axis'])
when(graphs).fetchAxisInfo('barplot', ...).thenReturn(responseAxisInfo['barplot_axis'])

when(sampler).retrieve_snippet('scatterplot').thenReturn(responseSnippet['scatterplot'])
when(sampler).retrieve_snippet('barplot').thenReturn(responseSnippet['barplot'])
when(sampler).retrieve_snippet('boxplot').thenReturn(responseSnippet['boxplot'])

def randomplot():
    responseRetrive = constants.mockPlots
    num_plots = randint(1,5)
    imgs = []
    for i in range(1,num_plots):
        img = ''+responseRetrive[randint(1,len(responseRetrive)-1)]
        imgs.append(img)
    return imgs

constants.mockPlots = generateMockPlots()
responseRetrieve['datetime'] = randomplot()
responseRetrieve['plot'] = randomplot()

when(mixin).fetchplotfromDBtimed(..., ...).thenReturn(responseRetrieve['datetime'])
when(mixin).fetchplotfromDB(..., ...).thenReturn(responseRetrieve['plot'])
