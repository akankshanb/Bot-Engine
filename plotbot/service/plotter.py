import framework.graphs as graphs
import framework.constants as constants
#import framework.mocking_agent
import controller.mmutil as mm
import framework.mixin as mixin


def scatterplotfunc(plot_details, dataset_filename):
    #print('in scatter')
    axis_info = graphs.fetchAxisInfo(plot_details)
    dataset = graphs.load_dataset('scatterplot', plot_details, dataset_filename)
    newGraph = graphs.scatter_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage(plot_details['user'], plot_details['dataset'])
    return newGraph.plotLocation

def barplotfunc(plot_details, dataset_filename):
    #print('in bar')
    axis_info = graphs.fetchAxisInfo(plot_details)
    dataset = graphs.load_dataset('barplot', plot_details, dataset_filename)
    newGraph = graphs.bar_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage(plot_details['user'], plot_details['dataset'])
    return newGraph.plotLocation


def boxplotfunc(plot_details, dataset_filename):
    #print('in box')
    axis_info = graphs.fetchAxisInfo(plot_details)
    dataset = graphs.load_dataset('boxplot', plot_details, dataset_filename)
    newGraph = graphs.box_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage(plot_details['user'], plot_details['dataset'])
    return newGraph.plotLocation

def plot(response, dsname):
    #text_list = input_txt.lower().strip().split()
    '''if len(text_list[1]) ==1:
        raise ValueError('Please give a plot type and file name')
    '''
    if response['plot_type'] in graph_dict.keys():
        filename = graph_dict[response['plot_type']](response, dsname)
        return_msg = "Here is your plots for **{}**".format(response['plot_type'])
        timestamp = mixin.getCurrentTimeStamp()
        print(filename)
        file_dict = {filename: timestamp}
        constants.metadata[response['user']][response['dataset']].update(file_dict)
        return return_msg, [filename]
    else: 
        raise ValueError('Please provide the correct plot type')
    
graph_dict = {"scatterplot":  scatterplotfunc, "barplot": barplotfunc, "boxplot": boxplotfunc} 
