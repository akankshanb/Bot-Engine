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
    if text_list[1] in graph_dict.keys():
        filename = graph_dict[text_list[1]]()
        print(filename)
        return "Here is you plot for **{}**".format(text_list[1])
    else:
        raise ValueError('A very specific bad thing happened')

graph_dict = {"scatterplot":  scatterplotfunc, "barplot": barplotfunc, "boxplot": boxplotfunc} 