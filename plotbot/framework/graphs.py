#!/usr/bin/env python3
import framework.mixin as mixin
#import framework.mocking_agent

def load_dataset(datasetname, plot_type):
    pass

def fetchAxisInfo(msg_arr, plot_type):
    pass

class graph(object):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    def __init__(self):
        self.plotID = self.generatePlotID()
        self.sns.set(style="darkgrid")
        self.axis_info = None
        self.plotLocation= ''
    
    def generatePlotID(self):
        plotID = mixin.generateID('plot')
        return plotID
    
    def saveimage(self):
        path = mixin.fetchDB_path()
        self.plotLocation=path+self.plotID+'.png'
        self.plt.savefig(self.plotLocation)
        self.plt.clf()
    
    def populate_axes_info(self):
        self.x_axis = self.axis_info['x-axis']
        self.y_axis = self.axis_info['y-axis']

class scatter_plot(graph):
    def __init__(self, dataset, axis_info):
        super(scatter_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info
        self.x_axis = axis_info['x-axis']
        self.y_axis = axis_info['y-axis']

    def plot_graph(self):
        self.populate_axes_info()
        self.sns.stripplot(x=self.x_axis, y=self.y_axis, data=self.data)

class box_plot(graph):
    def __init__(self, dataset, axis_info):
        super(box_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info
        self.x_axis = axis_info['x-axis']
        self.y_axis = axis_info['y-axis']


    def plot_graph(self):
        self.populate_axes_info(self.axis_info)
        self.sns.boxplot(x=self.x_axis)

class bar_plot(graph):
    def __init__(self, dataset, axis_info):
        super(bar_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info
        self.x_axis = axis_info['x-axis']
        self.y_axis = axis_info['y-axis']

    def plot_graph(self):
        self.populate_axes_info(self.axis_info)
        self.sns.stripplot(x=self.x_axis, y=self.y_axis, data=self.data)
