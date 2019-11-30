#!/usr/bin/env python3
import framework.mixin as mixin
import framework.constants as constants
#import framework.mocking_agent
from pandas import DataFrame
import  pandas as  pd
import numpy as np
import random

def load_dataset(plot_type, plot_details, datasetname):
    dataset_location = constants.cwd+'/'+constants.baseStorage+plot_details['user']+'/'+plot_details['dataset']+'/'+str(datasetname)+'.csv'
    df = pd.read_csv(dataset_location)
    return df

def fetchAxisInfo(graph_details):
    axis_info={
            'x-axis':   graph_details['x_axis'],
            'y-axis':   graph_details['y_axis']
    }
    print(axis_info)
    return axis_info

class graph(object):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    def __init__(self):
        self.plotID = self.generatePlotID()
        #self.sns.set(style="darkgrid")
        self.axis_info = None
        self.plotLocation= ''
        self.graphColors = []
    
    def generatePlotID(self):
        plotID = mixin.generateID('plot')
        return plotID
    
    def getPlotColor(self):
        random_col_index = random.randint(0,len(constants.color_pallet))
        if random_col_index not in self.graphColors:
            self.graphColors.append(random_col_index)
            color = constants.color_pallet[random_col_index]
            print(color)
            return color
        else:
            getPlotColor()
    
    def saveimage(self, user, dataset):
        path = dataset_location = constants.cwd+'/'+constants.baseStorage+user+'/'+dataset+'/'
        self.plotLocation=path+self.plotID+'.png'
        self.plt.savefig(self.plotLocation)
        self.plt.clf()
    
    def populate_axes_info(self):
        if self.axis_info['x-axis'] is not None:
            self.x_axis = self.axis_info['x-axis'][0]
        else:  self.x_axis = None 
        self.y_axis = self.axis_info['y-axis']

class scatter_plot(graph):
    def __init__(self, dataset, axis_info):
        super(scatter_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info

    def plot_graph(self):
        self.populate_axes_info()
        for y_axis in self.y_axis:
            plot_colour = self.getPlotColor()
            plot = self.sns.scatterplot(x=self.x_axis, y=y_axis, data=self.data, color=plot_colour)
            plot.set(xlabel=self.x_axis, ylabel=','.join(self.y_axis))

class box_plot(graph):
    def __init__(self, dataset, axis_info):
        super(box_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info

    def plot_graph(self):
        self.populate_axes_info()
        for y_axis in self.y_axis:
            plot_colour = self.getPlotColor()
            if self.x_axis is not None:   plot = self.sns.boxplot(x=self.x_axis, y=y_axis, data=self.data, color=plot_colour)
            else:   plot = self.sns.boxplot(x=y_axis, data=self.data, color=plot_colour)
            plot.set(xlabel=self.x_axis, ylabel=','.join(self.y_axis))
        
class bar_plot(graph):
    def __init__(self, dataset, axis_info):
        super(bar_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info

    def plot_graph(self):
        self.populate_axes_info()
        for y_axis in self.y_axis:
            plot_colour = self.getPlotColor()
            plot = self.sns.barplot(x=self.x_axis, y=y_axis, data=self.data, color=plot_colour)
            plot.set(xlabel=self.x_axis, ylabel=','.join(self.y_axis))
