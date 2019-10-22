def scatterplotfunc():
    print('in scatter')
    return "scatter <file_PATH>"
    #plot graph code goes here
def barplotfunc():
    print('in bar')
    return "bar <file_PATH>"
    #plot graph code goes here
def boxplotfunc():
    print('in box')
    return "box <file_PATH>"
    #plot graph code goes here

def plot(input_txt):
    text_list = input_txt.lower().strip().split()
    if len(text_list) ==1:
        raise ValueError('Please give a plot type and file name')
    elif len(text_list) ==2:
        raise ValueError('Please give a file name')
    else:
        if text_list[1] in graph_dict.keys():
            filename = graph_dict[text_list[1]]()
            return "Here is your plot for **{}**".format(text_list[1])
        else:
            raise ValueError('Please provide the correct plot type')
    

graph_dict = {"scatterplot":  scatterplotfunc, "barplot": barplotfunc, "boxplot": boxplotfunc} 