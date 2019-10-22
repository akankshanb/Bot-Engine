#!/usr/bin/env python3
import mixin

def load_dataset(datasetname, plot_type):
    pass

def fetchAxisInfo(msg_arr):
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
    
    def generatePlotID(self):
        plotID = mixin.generateID('plot')
        return plotID
    
    def saveimage(self):
        path = mixin.fetchDB_path()
        self.plt.savefig(path+self.plotID+'.png')
        self.plt.clf()
    
    def populate_axes_info(self):
        self.x_axis = self.axis_info['x-axis']
        self.y_axis = self.axis_info['y-axis']

class scatter_plot(graph):
    def __init__(self, dataset, axis_info):
        super(scatter_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info
        self.x_axis = None
        self.y_axis = None

    def plot_graph(self):
        self.populate_axes_info()
        self.sns.stripplot(x=self.x_axis, y=self.y_axis, data=self.data)

class box_plot(graph):
    def __init__(self, dataset, axis_info):
        super(box_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info
        self.x_axis = None
        self.y_axis = None


    def plot_graph(self):
        self.populate_axes_info(self.axis_info)
        self.sns.boxplot(x=self.x_axis)

class bar_plot(graph):
    def __init__(self, dataset, axis_info):
        super(bar_plot, self).__init__()
        self.data = dataset
        self.axis_info = axis_info
        self.x_axis = None
        self.y_axis = None

    def plot_graph(self):
        self.populate_axes_info(self.axis_info)
        self.sns.stripplot(x=self.x_axis, y=self.y_axis, data=self.data)
