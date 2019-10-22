import framework.graphs as graphs
import framework.constants as constants
import framework.mocking_agent

def scatterplotfunc(msg_arr, dataset_filename):
    print('in scatter')
    axis_info = graphs.fetchAxisInfo('scatterplot', msg_arr)
    dataset = graphs.load_dataset('scatterplot', dataset_filename)
    newGraph = graphs.scatter_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage()
    return newGraph.plotLocation

def barplotfunc(msg_arr, dataset_filename):
    print('in bar')
    axis_info = graphs.fetchAxisInfo('barplot', msg_arr)
    dataset = graphs.load_dataset('barplot', dataset_filename)
    newGraph = graphs.bar_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage()
    return newGraph.plotLocation


def boxplotfunc(msg_arr, dataset_filename):
    print('in box')
    axis_info = graphs.fetchAxisInfo('boxplot', msg_arr)
    dataset = graphs.load_dataset('boxplot', dataset_filename)
    newGraph = graphs.box_plot(dataset, axis_info)
    newGraph.plot_graph()
    newGraph.saveimage()
    return newGraph.plotLocation

def plot(input_txt, file_ids):
    text_list = input_txt.lower().strip().split()

    if len(text_list) ==1:
        raise ValueError('Please give a plot type and file name')
    elif len(text_list) ==2:
        raise ValueError('Please give a file name')

    if text_list[1] in graph_dict.keys():
        print(text_list)
        filename = graph_dict[text_list[1]](text_list[2:], file_ids)
        print(filename)
        return_msg = "Here is you plot for **{}**".format(text_list[1])
        return return_msg, [filename]
    else: 
        raise ValueError('Please provide the correct plot type')
    

graph_dict = {"scatterplot":  scatterplotfunc, "barplot": barplotfunc, "boxplot": boxplotfunc} 
