#!/usr/bin/env python3
import mixin


class user(object):
    def __init__(self, userid):
        self.userID = userid
        self.plotID = self.fetchPlots()
    
    def fetchPlots(self):
        return []


class graph(object):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    def __init__(self):
        self.plotID = self.generatePlotID()
        self.sns.set(style="darkgrid")
    
    def generatePlotID(self):
        plotID = mixin.generateID('plot')
        return plotID
    
    def saveimage(self):
        self.plt.savefig('allplots/'+self.plotID+'.png')
        self.plt.clf()
        pass

class scatter_plot(graph):
    def __init__(self, dataset):
        super(scatter_plot, self).__init__()
        self.datasetID = dataset

    def load_dataset(self):
        # for mocks using in-built dataset, actual implementation will use mentioned dataset
        self.data = self.sns.load_dataset(self.datasetID)

    def populate_axes_info(self):
        # for mocks using in-built dataset, actual implementation will use mentioned dataset
        self.x_axis = 'species'
        self.y_axis = 'petal_length'


    def plot_graph(self):
        self.load_dataset()
        self.populate_axes_info()
        self.sns.stripplot(x=self.x_axis, y=self.y_axis, data=self.data)

class box_plot(graph):
    def __init__(self, dataset):
        super(box_plot, self).__init__()
        self.datasetID = dataset

    def load_dataset(self):
        # for mocks using in-built dataset, actual implementation will use mentioned dataset
        self.data = self.sns.load_dataset(self.datasetID)
        
    def populate_axes_info(self):
        # for mocks using in-built dataset, actual implementation will use mentioned dataset
        self.x_axis = self.data["total_bill"]

    def plot_graph(self):
        self.load_dataset()
        self.populate_axes_info()
        self.sns.boxplot(x=self.x_axis)

class bar_plot(graph):
    def __init__(self, dataset):
        super(bar_plot, self).__init__()


    def load_dataset(self):
        # for mocks using in-built dataset, actual implementation will use mentioned dataset
        self.data = self.sns.load_dataset(self.datasetID)
        
    def populate_axes_info(self):
        # for mocks using in-built dataset, actual implementation will use mentioned dataset
        self.x_axis = 'species'
        self.y_axis = 'petal_length'
        
    def plot_graph(self):
        self.load_dataset()
        self.populate_axes_info()
        self.sns.stripplot(x=self.x_axis, y=self.y_axis, data=self.data)
