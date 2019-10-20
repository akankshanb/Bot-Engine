#!/usr/bin/env python3
import plotter
import re
botname = 'plotbot'
#intention = {}
'''
'main' = plot    or   retrive
'sub'  = dataset or   plotID
'plot_type' = scatter, pie, etc
'''

def reply_back(solution):
    pass

def parse_message(input_string):
    #tokens = preprocess_request(input_string)
    solution = None
    #user = input_string['user']
    intention = fetch_intention(input_string['text'])
    if len(intention) != 0:
        solution = intentionAction(intention)
    if solution is not None:
        reply_back(solution)

def fetch_intention(message):
    global botname
    intention = {}
    m = re.search(botname+' (\S+) (\S+) (\S+)',message)
    n = re.search(botname+' (\S+) (\S+)',message)
    if m is not None:
        intention['main'] = m.group(1)
        intention['sub'] = m.group(2)
        intention['plot_type'] = m.group(3)
    if n is not None:
        intention['main'] = m.group(1)
        intention['sub'] = m.group(2)
    return intention

def intentionAction(intention):
    solution = None
    if intention['main'] =='plot':
        solution = plotGraphs(intention)
    elif intention['main'] == 'retrive':
        solution = retriveGraph(intention)
    return solution
    
def plotGraphs(intention):
    dataset = intention['sub']
    graph_type = intention['plot_type']
    newGraph = None
    print(intention)
    if graph_type == 'scatter':
        newGraph = plotter.scatter_plot(dataset)
        newGraph.plot_graph()
        newGraph.saveimage()
    elif graph_type == 'pie':
        pass
    if newGraph is not None:    return newGraph.plotID
    else:   return None

def retriveGraph(intention):
    return None