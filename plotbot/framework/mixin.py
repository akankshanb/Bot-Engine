#!/usr/bin/env python3
import string
import random
import pickle
import constants

class ID(object):
    def __init__(self):
        self.plotIDs = []
        self.userIDs = []

def saveIDs(idtype, ids):
    filename = idtype+'_ids.db'
    outfile = open(filename,'wb')
    pickle.dump(ids,outfile)
    outfile.close()

def gatherIDs(idtype):
    filename = idtype+'_ids.db'
    infile = open(filename,'rb')
    ids = pickle.load(infile)
    infile.close()
    return ids

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    id= ''.join(random.choice(letters) for i in range(stringLength))
    return id

def generateID(idtype):
    if idtype=='plot':
        id = randomString()
        if id in constants.plotIDs:   generateID('plot')
        constants.plotIDs.append(id)
        saveIDs('plot', constants.plotIDs)
    elif idtype=='user':
        id = randomString()
        if id in constants.userIDs:   generateID('user')
        constants.userIDs.append(id)
        saveIDs('user', constants.userIDs)
    return id

instanceIDs = ID()
instanceIDs.plotIDs = gatherIDs('plot')

def fetchDB_path():
    pass

def fetchData(task):
    graphtype = task[0]
    action = task[1]
    if action == 'plot':
        newGraph = None
        if graphtype == 'scatter':  newGraph = constants.plotter.scatter_plot(constants.dataset)
        elif graphtype == 'box':  newGraph = constants.plotter.box_plot(constants.dataset)
        elif graphtype == 'bar':  newGraph = constants.plotter.bar_plot(constants.dataset)
        newGraph.plot_graph()
        newGraph.saveimage()
<<<<<<< HEAD
        @patch('plotter.graph.plotID', return_value='sadwdw')
=======
>>>>>>> mocking trail 3
        return str(newGraph.plotID)+'.png'
    elif action == 'snippet':
        filename = ''
        if graphtype == 'scatter': filename = constants.snippetter.scatter_plot()
        elif graphtype == 'box': filename = constants.snippetter.box_plot()
        elif graphtype == 'bar': filename = constants.snippetter.bar_plot()
        return filename

